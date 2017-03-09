from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.distance import vincenty
import numpy as np
import final_indexer
import reviews
import json
import string
import re

day_dic = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, \
'Friday': 5, 'Saturday': 6}
been_to_dic = {'Yusho': 4, 'bellyQ': 3, 'Xoco': 4}
address = '6031 South Ellis Ave'
max_distance = 5
dietary_restriction = ['Vegetarian', 'Halal']
time = 'Monday 1800'
username = 'Liz'
keywords = []
parsed_reviews = final_indexer.parse_reviews()
reviews_file = 'full_reviews.json'
ph_file = 'google_ph.json'
yelp = 'yelp_data.json'
with open(reviews_file, 'r') as f:
    data = f.read()
reviews_index = json.loads(data)

with open(ph_file, 'r') as f:
    data = f.read()
ph_index = json.loads(data)

with open(yelp, 'r') as f:
    data = f.read()
yelp_results = json.loads(data)

data_dic = final_indexer.get_large_index(parsed_reviews, ph_index, yelp_results)

if time:
    match = re.search("([\w]+)( )([\d]+)", time)
    day = match.group(1)
    hour = float(match.group(3))



def locate(day, hour, data_dic, user_lat, user_lon, max_distance):
    located_restaurants = {}
    if user_lat is not None and hour is not None:
        for restaurant, sub_dic in data_dic.items():
            lat2 = sub_dic['location'].get('latitude', 0)
            lon2 = sub_dic['location'].get('longitude', 0)
            miles = vincenty((user_lat, user_lon), (lat2, lon2)).miles
            closing_hr = 2400
            opening_hr = 0
            if 'hours' in sub_dic and 'close' in sub_dic['hours'] and 'open' in sub_dic['hours']: 
                closing_hr = float(sub_dic['hours'][day_dic[day]]['close']['time'])
                opening_hr = float(sub_dic['hours'][day_dic[day]]['open']['time'])
            if miles <= max_distance and hour <= closing_hr and hour >= opening_hr:
                located_restaurants[restaurant] = sub_dic
                located_restaurants[restaurant]['distance'] = miles
    elif hour is not None:
        for restaurant, sub_dic in data_dic.items():
            closing_hr = 2400
            opening_hr = 0
            if 'hours' in sub_dic and 'close' in sub_dic['hours'] and 'open' in sub_dic['hours']: 
                closing_hr = float(sub_dic['hours'][day_dic[day]]['close']['time'])
                opening_hr = float(sub_dic['hours'][day_dic[day]]['open']['time'])
            if hour <= closing_hr and hour >= opening_hr:
                located_restaurants[restaurant] = sub_dic
                located_restaurants[restaurant]['distance'] = miles
    elif user_lat is not None:
        for restaurant, sub_dic in data_dic.items():
            lat2 = sub_dic['location']['latitude']
            lon2 = sub_dic['location']['longitude']
            miles = vincenty((user_lat, user_lon), (lat2, lon2)).miles
            if miles <= max_distance:
                located_restaurants[restaurant] = sub_dic
                located_restaurants[restaurant]['distance'] = miles
    else:
        return data_dic
    return located_restaurants

def extract_preference(been_to_dic, data_dic):
        '''
        Gives the cuisine preference dicionary mapping cuisines to scores according to the user's
        history and the average price
        '''
        cuisine_preference_dic = {}
        #rating_lst = []
        price_lst =[]
        score_lst = []
        #size = 0 #records the occurence of cuisines with repeition
        for restaurant, score in been_to_dic.items():
            #rating_lst.append(data_dic[restaurant]['rating'])
            price_lst.append(data_dic[restaurant].get('price', 0))
            cuisine_lst = data_dic[restaurant]['cuisine']
            #size += len(cuisine_lst)
            score_lst = score_lst + [score] * len(cuisine_lst)
            for cuisine in cuisine_lst:
                cuisine_preference_dic[cuisine] = cuisine_preference_dic.get(cuisine, 0) + score
        mean_score = np.mean(score_lst)
        cuisine_preference_dic.update((cuisine, score/mean_score) for cuisine, score in cuisine_preference_dic.items())
        avg_price = np.mean(price_lst)
        #avg_rating = np.mean(rating_lst)
        return cuisine_preference_dic, avg_price

cuisine_preference_dic = extract_preference(been_to_dic, data_dic)[0]
avg_price = extract_preference(been_to_dic, data_dic)[1]

def generate_recommendation(day, hour, data_dic, user_lat, user_lon, max_distance, been_to_dic, dietary_restriction, avg_price):
    located_restaurants = locate(day, hour, data_dic, user_lat, user_lon, max_distance)
    recommendation_lst = []
    for restaurant, sub_dic in located_restaurants.items():
            cuisine_lst = sub_dic['cuisine']
            cuisine_score = 0
            dietary_restriction_multiplier = 1
            if 'parsed_reviews' in sub_dic:
                reviews = sub_dic['parsed_reviews']
                for restriction in dietary_restriction:
                    dietary_restriction_multiplier += reviews['dietary_restriction'].get(restriction, 0) / 5
            for cuisine in cuisine_lst:                    
                cuisine_score += cuisine_preference_dic.get(cuisine, 0)#It is possible that 'vegetarian' shows up in the cuisine list but not in the reviews
            cuisine_score = 5 * cuisine_score / len(cuisine_lst)
            
            price = sub_dic.get('price', 0) #needs price in data
            price_score = 4 - abs(avg_price - price)
            rating_score = sub_dic['rating']
            keywords_score = 0
            #for keywords in keywords:
                #keywords_score += reviews.get(keyword, 0) / 5
            distance = sub_dic['distance']
            been_to_score = 0
            if restaurant in been_to_dic:
                been_to_score = 1
            # round the sum of cuisine score and price score to the nearest integer
            recommendation_lst.append({'restaurant': restaurant, 'cuisine_score':cuisine_score, \
                'price_score': price_score, 'rating_score': rating_score, 'keywords_score': \
                keywords_score, 'distance': distance, 'been_to_score': been_to_score, \
                'cuisine_lst': cuisine_lst, 'price': price, 'dietary_restriction_multiplier': \
                dietary_restriction_multiplier})
        
    recommendation_lst = sorted(sorted(sorted(sorted(sorted(recommendation_lst, key=lambda \
        item:item['distance']), key=lambda item:item['keywords_score'], \
    reverse=True),key=lambda item:item['rating_score'], reverse=True), key=lambda \
    item:round(item['cuisine_score']*item['dietary_restriction_multiplier']+item['price_score'], 0), \
    reverse=True), key=lambda item:item['been_to_score'])
        
    return recommendation_lst[0], recommendation_lst






