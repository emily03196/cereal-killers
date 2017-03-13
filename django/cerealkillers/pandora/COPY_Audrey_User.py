from math import radians, cos, sin, asin, sqrt
import json
import numpy as np
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.distance import vincenty
import re
from . import COPY_An_indexer

data_file = 'pandora/COPY_final_completed_index.json'
with open(data_file, 'r') as f:
    data = f.read()
data_dic = json.loads(data)

been_to_dic = {'bistronomic': 4, 'Yum Cha': 3, 'Zoku Sushi': 5, 'Wildfire - Chicago': 4}
address = '6031 South Ellis Ave'
max_distance = 20
dietary_restriction = ['Vegetarian']
time = 'Monday 1800'
username = 'Liz'
keywords = {'environment': None, 'service': None, 'waiting': None}


class User:

    data_dic = data_dic
    
    def __init__(self, username, address, time, dietary_restriction, max_distance, been_to_dic, \
        keywords):
        self.user_lat = None #None or numerical
        self.user_lon = None #None or numerical
        self.max_distance = None #None or numerical
        self.address = address #None or string
        self.dietary_restriction = []
        self.keywords = {} #dictionary
        self.day = None #None or string
        self.hour = None #None or string

        if address: 
            location = geolocator.geocode(address)
            self.user_lat = location.latitude
            self.user_lon = location.longitude
        if max_distance:
            self.max_distance = max_distance
        if dietary_restriction:
            self.dietary_restriction = dietary_restriction
        if time:
            match = re.search("([\w]+)( )([\d]+)", time)
            self.day = match.group(1)
            self.hour = float(match.group(3))
        if keywords:
            self.keywords = keywords
        
        self.been_to_dic = been_to_dic
        self.cuisine_preference_dic = self.extract_preference()[0]
        self.avg_price = self.extract_preference()[1]
        self.username = username

    def locate(self):
        '''
        Gives a dictionary of restaurants that are within the maximal distance from the user and 
        that are open
        '''
        located_restaurants = {}
        if self.user_lat is not None and self.hour is not None:
            for restaurant, sub_dic in self.data_dic.items():
                lat2 = sub_dic['location'].get('lat', 0)#some restaurants don't have locations/latitude
                lon2 = sub_dic['location'].get('lon', 0)
                miles = vincenty((self.user_lat, self.user_lon), (lat2, lon2)).miles
                closing_hr = 2400#some restaurants don't have hours
                opening_hr = 0
                hours = sub_dic['hours']
                if self.day in sub_dic['hours']: 
                    closing_hr = float(hours[self.day][0])
                    opening_hr = float(hours[self.day][1])
                if miles <= self.max_distance and self.hour <= closing_hr and self.hour >= opening_hr:       
                    located_restaurants[restaurant] = sub_dic
                    located_restaurants[restaurant]['distance'] = miles
        elif self.hour is not None:
            for restaurant, sub_dic in self.data_dic.items():
                closing_hr = 2400
                opening_hr = 0
                hours = sub_dic['hours']
                if self.day in sub_dic['hours']: 
                    closing_hr = float(hours[self.day][0])
                    opening_hr = float(hours[self.day][1])
                if self.hour <= closing_hr and self.hour >= opening_hr:
                    located_restaurants[restaurant] = sub_dic
                    located_restaurants[restaurant]['distance'] = miles
        elif self.user_lat is not None:
            for restaurant, sub_dic in self.data_dic.items():
                lat2 = sub_dic.get('location', {}).get('lat', 0)#some restaurants don't have locations/latitude
                lon2 = sub_dic.get('location', {}).get('lon', 0)
                miles = vincenty((self.user_lat, self.user_lon), (lat2, lon2)).miles
                if miles <= self.max_distance:
                    located_restaurants[restaurant] = sub_dic
                    located_restaurants[restaurant]['distance'] = miles
        else:
            return self.data_dic
        return located_restaurants

    def extract_preference(self):
        '''
        Gives the cuisine preference dicionary mapping cuisines to scores according to the user's
        history and the average price
        '''
        cuisine_preference_dic = {}
        price_lst =[]
        score_lst = []
        for restaurant, score in self.been_to_dic.items():
            price_lst.append(self.data_dic[restaurant].get('price', 0))
            cuisine_lst = self.data_dic[restaurant].get('cuisine', [])
            score_lst = score_lst + [score] * len(cuisine_lst)
            for cuisine in cuisine_lst:
                cuisine_preference_dic[cuisine] = cuisine_preference_dic.get(cuisine, 0) + score
        mean_score = np.mean(score_lst)
        cuisine_preference_dic.update((cuisine, score/mean_score) for cuisine, score in cuisine_preference_dic.items())
        avg_price = np.mean(price_lst)
        return cuisine_preference_dic, avg_price
 
    def generate_recommendation(self):
        '''
        Gives a tuple of a recommendation in the format of dictionary and a recommendation list
        '''
        located_restaurants = self.locate()
        recommendation_lst = []
        
        for restaurant, sub_dic in located_restaurants.items():
            address = sub_dic.get('address', '')
            phone = sub_dic.get('phone', '')
            cuisine_lst = sub_dic.get('cuisine', [])
            cuisine_score = 0
            dietary_restriction_multiplier = 1
            keywords_multiplier = 1
            if 'analyzed_reviews' in sub_dic:
                reviews = sub_dic['analyzed_reviews']
                for restriction in self.dietary_restriction:
                    if restriction in reviews.get('dietary_choices', []):
                        dietary_restriction_multiplier += 1/5
                for keyword, value in keywords.items():
                    if value is True:
                        keywords_multiplier += reviews.get(keyword+'_score', 0)
            if len(cuisine_lst) > 0:
                for cuisine in cuisine_lst:                    
                    cuisine_score += self.cuisine_preference_dic.get(cuisine, 0)#It is possible that 'vegetarian' shows up in the cuisine list but not in the reviews
                cuisine_score = 5 * cuisine_score / len(cuisine_lst)            
            price = sub_dic.get('price', 0)
            price_score = 4 - abs(self.avg_price - price)
            rating_score = sub_dic['rating']
            distance = sub_dic['distance']
            been_to_score = 0
            if restaurant in been_to_dic:
                been_to_score = 1
            # round the sum of cuisine score and price score to the nearest integer
            recommendation_lst.append({'restaurant': restaurant, 'cuisine_score':cuisine_score, \
                'price_score': price_score, 'rating_score': rating_score, 'keywords_multiplier': \
                keywords_multiplier, 'distance': distance, 'been_to_score': been_to_score, \
                'cuisine_lst': cuisine_lst, 'price': price, 'dietary_restriction_multiplier': \
                dietary_restriction_multiplier, 'address': address, 'phone': phone})
        
        recommendation_lst = sorted(sorted(sorted(sorted(recommendation_lst, \
            key=lambda item:item['distance']),key=lambda item:item['rating_score'], reverse=True), key=lambda \
        item:round(item['cuisine_score']*item['dietary_restriction_multiplier']*item['keywords_multiplier']\
            +item['price_score'], 0), reverse=True), key=lambda item:item['been_to_score'])
        
        if len(recommendation_lst) == 0:
            return 'No Options', recommendation_lst
        return recommendation_lst[0], recommendation_lst

    def reject(self, recommendation_lst, not_cuisine, price_too_high, price_too_low):
        rejected_rec = recommendation_lst[0]
        rejected_price = rejected_rec['price']
        recommendation_lst = recommendation_lst[1:]
        if not_cuisine is None and price_too_high is None and price_too_low is None:
            if len(recommendation_lst) == 0:
                return 'No Options', recommendation_lst
            else:
                return recommendation_lst[0], recommendation_lst
        else:
            if not_cuisine is True:
                disliked_cuisine_lst = rejected_rec['cuisine_lst']
                size = len(disliked_cuisine_lst)
                for rec in recommendation_lst:
                    cuisine_lst = rec['cuisine_lst']
                    cuisine_score = rec['cuisine_score']
                    for cuisine in cuisine_lst:
                        if cuisine in disliked_cuisine_lst:
                            cuisine_score -= 5*self.cuisine_preference_dic.get(cuisine,0)/len(cuisine_lst)\
                             - 1/len(cuisine_lst) #needs to rethink how much to subtract
                    rec['cuisine_score'] = cuisine_score
            if price_too_high is True:
                recommendation_lst = [recommendation for recommendation in recommendation_lst if \
                recommendation['price'] < rejected_price]
            if price_too_low is True:
                recommendation_lst = [recommendation for recommendation in recommendation_lst if \
                recommendation['price'] > rejected_price]
            
            recommendation_lst = sorted(sorted(sorted(sorted(recommendation_lst, 
                key=lambda item:item['distance']),key=lambda item:item['rating_score'], reverse=True), key=lambda 
            item:round(item['cuisine_score']*item['dietary_restriction_multiplier']*item['keywords_multiplier']
                +item['price_score'], 0), reverse=True), key=lambda item:item['been_to_score'])          

            if len(recommendation_lst) == 0:
                return 'No Options', recommendation_lst
            else:
                return recommendation_lst[0], recommendation_lst

    def modify_address(self, new_address):
        self.user_lat = None
        self.user_lon = None
        self.address = new_address
        if new_address:
            location = geolocator.geocode(new_address)
            self.user_lat = location.latitude
            self.user_lon = location.longitude
        #need to call locate again (automatically included in generate_recommendation)

    def modify_distance(self, new_max_distance):
        self.max_distance = new_max_distance
        #need to call locate again (automatically included in generate_recommendation)

    def modify_time(self, new_time):
        self.day = None
        self.hour = None
        if new_time:
            match = re.search("([\w]+)( )([\d]+)", new_time)
            self.day = match.group(1)
            self.hour = match.group(3)
            #need to call locate again (automatically included in generate_recommendation)

    def modify_history(self, new_been_to_dic):
        self.been_to_dic = new_been_to_dic
        self.cuisine_preference_dic = self.extract_preference()[0]
        self.avg_price = self.extract_preference()[1]

    def modify_dietary_restriction(self, new_dietary_restriction):
        self.dietary_restriction = dietary_restriction

    def modify_keywords(self, new_keywords):
        self.keywords = new_keywords
        
    def accept(self, rec):
        return self.username, self.been_to_dic, self.address, rec

#helpful reviews or most recent reviews
#user puts in single word, bigrams. 
#put in dumplings. show the part of the reviews. 