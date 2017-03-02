from math import radians, cos, sin, asin, sqrt
import json
import Audrey_util
import numpy as np

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

been_to_dic = {'The Purple Pig': 4, 'Animale': 5}
location_requirement_dic = {'user_lat': '41.78502539999999', 'user_lon': '-87.60034869999998', 'max_distance':10}
data_file = 'sample_data.json'

with open(data_file, 'r') as f:
    data = f.read()
data = data.replace('\n ', '')
data = data.replace("'", '"')
data_dic = json.loads(data)


def locate(location_requirement_dic, data_dic):
    user_lat = location_requirement_dic['user_lat'] #string
    user_lon = location_requirement_dic['user_lon'] #string
    max_distance = location_requirement_dic['max_distance'] #float
    located_restaurants = {}
    for restaurant, sub_dic in data_dic.items():
        lat2 = sub_dic['location']['latitude']
        lon2 = sub_dic['location']['longitude']
        #miles = Audrey_util.haversine(float(user_lat), float(user_lon), lat2, lon2) * 1.609344
        lat2 = str(lat2)
        lon2 = str(lon2)
        miles = Audrey_util.compute_distance(user_lat, user_lon, lat2, lon2)
        miles = float(miles)
        if miles <= max_distance:
            located_restaurants[restaurant] = sub_dic
            located_restaurants[restaurant]['distance'] = miles
    return located_restaurants


def extract_preference(been_to_dic, data_dic):
    cuisine_preference_dic = {}
    rating_lst = []
    price_lst =[]
    score_lst = []
    size = len(been_to_dic)

    for restaurant, score in been_to_dic.items():
        score_lst.append(score)
        #rating_lst.append(data_dic[restaurant]['rating'])
        #price_lst.append(data_dic[restaurant]['price'])
        cuisine_lst = data_dic[restaurant]['cuisine']
        for cuisine in cuisine_lst:
            cuisine_preference_dic[cuisine] = cuisine_preference_dic.get(cuisine, 0) + score/size

    #avg_price = np.mean(price_lst)
    #avg_rating = np.mean(rating_lst)

    return cuisine_preference_dic
 

def generate_recommendation(been_to_dic, location_requirement_dic, data_dic):
    located_restaurants = locate(location_requirement_dic, data_dic)
    cuisine_preference_dic = extract_preference(been_to_dic, data_dic)
    recommendation_lst = []
    been_to_lst = []
    for restaurant, sub_dic in located_restaurants.items():
        cuisine_lst = sub_dic['cuisine']
        cuisine_score = 0
        for cuisine in cuisine_lst:
            cuisine_score += cuisine_preference_dic.get(cuisine, 0)
            cuisine_score = cuisine_score/len(cuisine_lst)
        print(cuisine_score)
        #price = sub_dic['price']
        #price_score = 4 - abs(avg_price - price)
        #print(rating_score)
        total_score = cuisine_score #+ price_score
        rating_score = sub_dic['rating']
        distance = sub_dic['distance']
        been_to_score = 0
        if restaurant in been_to_dic:
            been_to_score = 1
        recommendation_lst.append((restaurant, total_score, rating_score, been_to_score, distance, cuisine_lst, price))
    recommendation_lst = sorted(sorted(sorted(sorted(recommendation_lst, key=lambda item:item[4]), key=lambda item:item[3]), key=lambda item:item[2], reverse=True), key=lambda item:item[1], reverse=True)
    return recommendation_lst[0], recommendation_lst


def rejection(recommendation_lst, been_to_lst, not_cuisine, price_too_high, price_too_low):
    if not_cuisine is None and price_too_high is None and price_too_low is None:
        recommendation_lst = recommendation_lst[1:]
        if len(recommendation_lst) == 0:
            return 'No Options'
        else:
            return recommendation_lst[0], recommendation_lst
    elif not_cuisine is None:
        price = recommendation_lst[0][6]
        if price_too_high is not None:
            recommendation_lst = [recommendation for recommendation in recommendation_lst if recommendation[6] < price]
            return recommendation_lst[0], recommendation_lst
        elif price_too_low is not None:
            recommendation_lst = [recommendation for recommendation in recommendation_lst if recommendation[6] > price]
            










'''
def generate_options(restaurant_lst, restaurant_dic, review_catalog, been_to_lst, requirement_dic):
    restaurant_lst_reduced = [restaurant in restaurant_lst if restaurant not in been_to_lst]
    
    cuisine = requirement_dic.get('cuisine', None)
    price_lower = requirement_dic.get('price_lower', None)
    price_upper = requirement_dic.get('price_upper', None)
    location = restaurant_dic.get('location', None)
    distance = restaurant_dic.get('distance', None)
    rating_lower = requirement_dic.get('ratin _lower', None)
    rating_upper = requirement_dic.get('rating_upper', None)

    options = [] 
    for restaurant in restaurant_lst_reduced:
        if cuisine is None or cuisine == restaurant_dic[restaurant]['cuisine']:
            C = True
        else:
            C = False
        if price_lower is None and price_upper is None:
            P = True
        elif price_lower is not None:
            if price_upper >= restaurant_dic[restaurant]['price_upper']:
                P = True
            else:
                P = False
        else:
            if price_lower <= restaurant_dic[restaurant]['price_lower']:
                P = True
            else:
                P = False
        if rating_lower is None and price_upper is None:
            R = True
        elif rating_lower is not None:
            if rating_upper >= restaurant_dic[restaurant]['rating_upper']:
                R = True
            else:
                R = False
        else:
            if rating_lower <= restaurant_dic[restaurant]['rating_lower']:
                R = True
            else:
                R = False
        if location is None and distance is None:
            D = True
        elif location is not None and distance is not None: 
            distance_calculated = calculate_distance(location, restaurant_dic[restaurant]['location'])
            if distance_calculated <= distance:
                D = True
            else:
                D = False
        if C and P and R and D:
            options.append(restaurant)
    return None
'''
