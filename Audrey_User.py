from math import radians, cos, sin, asin, sqrt
import json
import Audrey_util
import numpy as np
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.distance import vincenty
import re


been_to_dic = {'Farmhouse': 4, 'Bar on Buena': 3, 'City  Cafe': 4}
address = '6031 South Ellis Ave'
location_requirement_dic = {'user_lat': '41.78502539999999', 'user_lon': '-87.60034869999998', 'max_distance':10}
data_file = 'sample_data.json'
user_data = 'user_data.csv'
time = 'Monday 1800'
dietary_restriction = ['Vegetarian', 'Halal']


with open(data_file, 'r') as f:
    data = f.read()
data = json.loads(data)

class User:

    data_dic = data
    
    def __init__(self, username, address, time, dietary_restriction, max_distance, been_to_dic):
        location = geolocator.geocode(address)
        self.user_lat = location.latitude
        self.user_lon = location.longitude
        self.max_distance = max_distance
        self.been_to_dic = been_to_dic
        self.cuisine_preference_dic = self.extract_preference()[0]
        self.avg_price = self.extract_preference()[1]
        self.username = username
        self.address = address
        self.dietary_restriction = dietary_restriction
        match = re.search("([\w]+)( )([\d]+)", time)
        self.day = match.group(1)
        self.hour = match.group(3)

    def locate(self):
        '''
        Gives a list of restaurants within the maximal distance from the user
        '''
        located_restaurants = {}
        for restaurant, sub_dic in self.data_dic.items():
            lat2 = sub_dic['location']['latitude']
            lon2 = sub_dic['location']['longitude']
            miles = vincenty((self.user_lat, self.user_lon), (lat2, lon2)).miles
            if miles <= self.max_distance and self.hour >= sub_dic['hours'][self.day][0] and self.hour <= sub_dic['hours'][self.day][1]:
                located_restaurants[restaurant] = sub_dic
                located_restaurants[restaurant]['distance'] = miles
        return located_restaurants

    def extract_preference(self):
        '''
        Gives the cuisine preference dicionary mapping cuisines to scores according to the user's
        history and the average price
        '''
        cuisine_preference_dic = {}
        #rating_lst = []
        price_lst =[]
        score_lst = []
        size = 0 #records the occurence of cuisines with repeition
        for restaurant, score in self.been_to_dic.items():
            #rating_lst.append(data_dic[restaurant]['rating'])
            price_lst.append(self.data_dic[restaurant].get('price', 0))
            cuisine_lst = self.data_dic[restaurant]['cuisine']
            size += len(cuisine_lst)
            score_lst = score_lst + [score] * len(cuisine_lst)
            for cuisine in cuisine_lst:
                cuisine_preference_dic[cuisine] = cuisine_preference_dic.get(cuisine, 0) + score
        mean_score = np.mean(score_lst)
        std = np.std(score_lst)#normalize scores
        cuisine_preference_dic.update((cuisine, (score - mean_score)/(std * size)) for cuisine, score in cuisine_preference_dic.items())
        avg_price = np.mean(price_lst)
        #avg_rating = np.mean(rating_lst)
        return cuisine_preference_dic, avg_price
 
    def generate_recommendation(self):
        '''
        Gives a tuple of a recommendation in the format of dictionary and a recommendation list
        '''
        located_restaurants = self.locate()
        recommendation_lst = []
        been_to_lst = []
        for restaurant, sub_dic in located_restaurants.items():
            cuisine_lst = sub_dic['cuisine']
            cuisine_score = 0
            dietary_restriction_score = 0
            for cuisine in cuisine_lst:
                cuisine_score += self.cuisine_preference_dic.get(cuisine, 0)
                if cuisine in self.dietary_restriction:
                    dietary_restriction_score += 1
            cuisine_score = 5 * cuisine_score/len(cuisine_lst)
            price = sub_dic.get('price', 0) #needs to price in data
            price_score = 4 - abs(self.avg_price - price)
            rating_score = sub_dic['rating']
            distance = sub_dic['distance']
            been_to_score = 0
            if restaurant in been_to_dic:
                been_to_score = 1
            dietary_restriction_score = 0
            if 
            recommendation_lst.append([restaurant, cuisine_score, price_score, rating_score, distance, been_to_score, cuisine_lst, price, dietary_restriction_score])
        recommendation_lst = sorted(sorted(sorted(sorted(sorted(recommendation_lst, key=lambda item:item[4]), key=lambda item:item[3], reverse = True), key=lambda item:item[1]+item[2], reverse=True), key=lambda item:item[8], reverse=True), key=lambda item:item[5])
        return recommendation_lst[0], recommendation_lst

    def reject(self, recommendation_lst, not_cuisine, price_too_high, price_too_low):
        rejected_rec = recommendation_lst[0]
        rejected_price = rejected_rec[7]
        recommendation_lst = recommendation_lst[1:]
        if not_cuisine is None and price_too_high is None and price_too_low is None:
            recommendation_lst = recommendation_lst[1:]
            if len(recommendation_lst) == 0:
                return 'No Options'
            else:
                return recommendation_lst[0], recommendation_lst
        else:
            if not_cuisine is True:
                disliked_cuisine_lst = rejected_rec[6]
                size = len(disliked_cuisine_lst)
                for rec in recommendation_lst:
                    cuisine_lst = rec[6]
                    cuisine_score = rec[1]
                    for cuisine in cuisine_lst:
                        if cuisine in disliked_cuisine_lst:
                            cuisine_score -= self.cuisine_preference_dic.get(cuisine,0) - 1/size #needs to rethink how much to subtract
                    rec[1] = cuisine_score
            if price_too_high is True:
                recommendation_lst = [recommendation for recommendation in recommendation_lst if recommendation[7] < rejected_price]
            if price_too_low is True:
                recommendation_lst = [recommendation for recommendation in recommendation_lst if recommendation[7] > rejected_price]
            recommendation_lst = sorted(sorted(sorted(sorted(sorted(recommendation_lst, key=lambda item:item[4]), key=lambda item:item[3], reverse = True), key=lambda item:item[1]+item[2], reverse=True), key=lambda item:item[8], reverse=True), key=lambda item:item[5])
            return recommendation_lst[0], recommendation_lst

    def modify_location(self, new_location_requirement_dic):
        self.user_lat = new_location_requirement_dic['user_lat'] #string
        self.user_lon = new_location_requirement_dic['user_lon'] #string
        self.max_distance = new_location_requirement_dic['max_distance'] #float
        #need to call locate again

    def modify_time(self, new_time):
        match = re.search("([\w]+)( )([\d]+)", new_time)
        self.day = match.group(1)
        self.hour = match.group(3)
        #need to call locate again

    def modify_history(self, new_been_to_dic):
        self.been_to_dic = new_been_to_dic
        self.cuisine_preference_dic = self.extract_preference()[0]
        self.avg_price = self.extract_preference()[1]

    def modify_dietary_restriction(self, new_dietary_restriction):
        self.dietary_restriction = dietary_restriction

    def accept(self, rec):
        return self.username, self.been_to_dic, self.address, rec
