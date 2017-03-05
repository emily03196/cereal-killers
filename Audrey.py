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
    located_restaurants_dic = {}
    for restaurant, sub_dic in data_dic.items():
        lat2 = sub_dic['location']['latitude']
        lon2 = sub_dic['location']['longitude']
        miles = Audrey_util.haversine(float(user_lat), float(user_lon), lat2, lon2) * 1.609344
        #lat2 = str(lat2)
        #lon2 = str(lon2)
        #miles = Audrey_util.compute_distance(user_lat, user_lon, lat2, lon2)
        #miles = float(miles)
        if miles <= max_distance:
            located_restaurants_dic[restaurant] = sub_dic
            located_restaurants_dic[restaurant]['distance'] = miles
    return located_restaurants_dic


def extract_preference(been_to_dic, data_dic):
    cuisine_preference_dic = {}
    #rating_lst = []
    price_lst =[]
    score_lst = []

    for restaurant, score in been_to_dic.items():
        score_lst.append(score)
        #rating_lst.append(data_dic[restaurant]['rating'])
        price_lst.append(data_dic[restaurant]['price'])
        cuisine_lst = data_dic[restaurant]['cuisine']
        for cuisine in cuisine_lst:
            cuisine_preference_dic[cuisine] = cuisine_preference_dic.get(cuisine, 0) + score
    size = len(cuisine_preference_dic)
    for cuisine in cuisine_preference_dic.keys():
        cuisine_preference_dic[cuisine] = cuisine_preference_dic[cuisine] / size

    avg_price = np.mean(price_lst)
    #avg_rating = np.mean(rating_lst)

    return cuisine_preference_dic, avg_price
 

def generate_recommendation(been_to_dic, location_requirement_dic, data_dic):
    located_restaurants_dic = locate(location_requirement_dic, data_dic)
    cuisine_preference_dic, avg_price = extract_preference(been_to_dic, data_dic)
    recommendation_lst = []
    been_to_lst = []
    print('avgprice', avg_price)
    for restaurant, sub_dic in located_restaurants.items():
        cuisine_lst = sub_dic['cuisine']
        cuisine_score = 0
        for cuisine in cuisine_lst:
            cuisine_score += cuisine_preference_dic.get(cuisine, 0)
            cuisine_score = cuisine_score / len(cuisine_lst)
        price = sub_dic['price']
        price_score = 4 - abs(avg_price - price)
        rating_score = sub_dic['rating']
        distance = sub_dic['distance']
        been_to_score = 0
        if restaurant in been_to_dic:
            been_to_score = 1
        recommendation_lst.append((restaurant, cuisine_score, price_score, rating_score, been_to_score, distance, cuisine_lst, price))
        print(restaurant, cuisine_score, price_score, rating_score, been_to_score, distance, cuisine_lst, price)
    recommendation_lst = sorted(sorted(sorted(sorted(recommendation_lst, key=lambda item:item[5]), key=lambda item:item[3], reverse=True), key=lambda item:item[1]+item[2], reverse=True), key=lambda item:item[4])
    return recommendation_lst[0][0], recommendation_lst


def rejection(recommendation_lst, been_to_lst, not_cuisine, price_too_high, price_too_low, cuisine_preference_dic):
    rejected_recommendation = recommendation_lst[0]
    recommendation_lst = recommendation_lst[1:]
    if not_cuisine is None and price_too_high is None and price_too_low is None:
        if len(recommendation_lst) == 0:
            return 'No Options'
        else:
            return recommendation_lst[0][0], recommendation_lst
    else:
        if not_cuisine is True:
            disliked_cuisine_lst = rejected_recommendation[6]
            size = len(disliked_cuisine_lst)  
            for recommendation in recommendation_lst:
                cuisine_lst = recommendation[6]
                cuisine_score = recommendation[1]
                for cuisine in cuisine_lst:
                    if cuisine in disliked_cuisine_lst:
                        cuisine_score -= cuisine_preference_dic.get(cuisine,0) - 1 / size
                recommendation[1] = cuisine_score
        if price_too_high is True:
            recommendation_lst = [recommendation for recommendation in recommendation_lst if recommendation[7] < price]
        if price_too_low is True:
            recommendation_lst = [recommendation for recommendation in recommendation_lst if recommendation[7] > price]
        recommendation_lst = sorted(sorted(sorted(sorted(recommendation_lst, key=lambda item:item[5]), key=lambda item:item[3], reverse=True), key=lambda item:item[1] + item[2], reverse=True), key=lambda item:item[4])
        return recommendation_lst[0][0], recommendation_lst










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
