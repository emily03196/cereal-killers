from math import radians, cos, sin, asin, sqrt
import json
import Audrey_util
import numpy as np
import csv

'''
User input:
1) A dictionary of restaurants (string) he's been to and rated
    keys: restaurant names
    values: scores
2) A dictionary with the following keys 'user_lat', 'user_long', 'max_distance'. 
Things we have:
A list of restaurant names (string)
A dictionary of dictionaries with restaurant names as keys, then each sub-dictionary containes the following keys 'cuisine' (a list of strings), 'price' (a value 1-4), 'location' (a dictionary 'address', latitude', 'longitude'), 'rating.
Review catalog: list of tuples (restaurant name, word)
'''

been_to_dic = {'Farmhouse': 4, 'Bar on Buena': 3, 'City  Cafe': 4}
location_requirement_dic = {'user_lat': '41.78502539999999', 'user_lon': '-87.60034869999998', 'max_distance':10}
data_file = 'sample_data.json'
user_data = 'user_data.csv'

with open(data_file, 'r') as f:
    data = f.read()
data = json.loads(data)

class User:

    data_dic = data
    
    def __init__(self, username, location_requirement_dic, been_to_dic):
        self.user_lat = location_requirement_dic['user_lat'] #string
        self.user_lon = location_requirement_dic['user_lon'] #string
        self.max_distance = location_requirement_dic['max_distance'] #float
        self.been_to_dic = been_to_dic
        self.cuisine_preference_dic = self.extract_preference()[0]
        self.avg_price = self.extract_preference()[1]
        self.final_rec = 
        self.username = username

    def locate(self):
        located_restaurants = {}
        for restaurant, sub_dic in self.data_dic.items():
            lat2 = sub_dic['location']['latitude']
            lon2 = sub_dic['location']['longitude']
            miles = Audrey_util.haversine(float(self.user_lon), float(self.user_lat), lon2, lat2) / 1.609344
            #lat2 = str(lat2)
            #lon2 = str(lon2)
            #miles = Audrey_util.compute_distance(user_lat, user_lon, lat2, lon2)
            #miles = float(miles)
            if miles <= self.max_distance:
                located_restaurants[restaurant] = sub_dic
                located_restaurants[restaurant]['distance'] = miles
        return located_restaurants

    def extract_preference(self):
        cuisine_preference_dic = {}
        #rating_lst = []
        price_lst =[]
        #score_lst = []
        size = 0
        for restaurant, score in self.been_to_dic.items():
            #score_lst.append(score)
            #rating_lst.append(data_dic[restaurant]['rating'])
            price_lst.append(self.data_dic[restaurant].get('price', 0))
            cuisine_lst = self.data_dic[restaurant]['cuisine']
            size += len(cuisine_lst)
            for cuisine in cuisine_lst:
                cuisine_preference_dic[cuisine] = cuisine_preference_dic.get(cuisine, 0) + score
        cuisine_preference_dic.update((cuisine, 2*score) for cuisine, score in cuisine_preference_dic.items())
        avg_price = np.mean(price_lst)
        #avg_rating = np.mean(rating_lst)
        return cuisine_preference_dic, avg_price
 
    def generate_recommendation(self):
        located_restaurants = self.locate()
        recommendation_lst = []
        been_to_lst = []
        for restaurant, sub_dic in located_restaurants.items():
            cuisine_lst = sub_dic['cuisine']
            cuisine_score = 0
            for cuisine in cuisine_lst:
                cuisine_score += self.cuisine_preference_dic.get(cuisine, 0)
                cuisine_score = cuisine_score/len(cuisine_lst)
            price = sub_dic.get('price', 0) #needs to price in data
            price_score = 4 - abs(self.avg_price - price)
            #total_score = cuisine_score + price_score
            rating_score = sub_dic['rating']
            distance = sub_dic['distance']
            been_to_score = 0
            if restaurant in been_to_dic:
                been_to_score = 1
            recommendation_lst.append([restaurant, cuisine_score, price_score, rating_score, distance, been_to_score, cuisine_lst, price])
        recommendation_lst = sorted(sorted(sorted(sorted(recommendation_lst, key=lambda item:item[4]), key=lambda item:item[3], reverse = True), key=lambda item:item[1]+item[2], reverse=True), key=lambda item:item[5])
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
            recommendation_lst = sorted(sorted(sorted(sorted(recommendation_lst, key=lambda item:item[4]), key=lambda item:item[3], reverse = True), key=lambda item:item[1]+item[2], reverse=True), key=lambda item:item[5])
            return recommendation_lst[0], recommendation_lst

    def change_location(self, new_location_requirement_dic):
        self.user_lat = new_location_requirement_dic['user_lat'] #string
        self.user_lon = new_location_requirement_dic['user_lon'] #string
        self.max_distance = new_location_requirement_dic['max_distance'] #float

    def accept(self, rec):
        self.final_rec = rec
        with open(user_data, 'a') as user_data:
            writer = csv.writer(user_data)
            writer.writerow([self.username, (self.location_requirement_dic['latitude'], self.location_requirement_dic['longitude']), self.been_to_dic, final_rec])
