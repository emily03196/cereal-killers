from math import radians, cos, sin, asin, sqrt
import json
import Audrey_util
import numpy as np
import csv

'''
Data:
1) A dictionary of dictionaries with restaurant names as keys, then each sub-dictionary 
containes the following keys 'cuisine' (a list of strings), 'price' (a value 0-4), 'location' 
(a dictionary 'address', latitude', 'longitude'), 'rating', 'hours', 'reviews'.
2) Review catalog: a dictionary of keys of restaurant names and values of lists of review strings
'''
data_file = 'sample_data.json'
with open(data_file, 'r') as f:
    data = f.read()
data = json.loads(data)

'''
User input:
1) A dictionary of restaurants (string) he's been to and rated with keys of restaurant names
   and values of scores (required)
2) User address (optional, required if maximal distance is entered)
3) Maximal distance (optional)
4) Dietary restrictions (optional)
5) Time (optional)
6) Username (required)
'''
#Test input
#user_data = 'user_data.csv'
been_to_dic = {'Yusho': 4, 'bellyQ': 3, 'Xoco': 4}
address = '6031 South Ellis Ave'
max_distance = 5
dietary_restriction = ['Vegetarian', 'Halal']
time = 'Monday 1800'
username = 'Liz'
keywords (optional)

user = Audrey_User.User(username = username, been_to_dic = been_to_dic, address = address, \
    max_distance = max_distance, time = time, dietary_restriction = dietary_restriction, \
    keywords = keywords)
recommendation, recommendation_lst = user.generate_recommendation()

#reject
if reject == True:
    recommendation, recommendation_lst = user.reject(recommendation_lst = recommendation_lst, \
        not_cuisine, price_too_high, price_too_low)
    
#accept
if reject == False:
    username, been_to_dic, address, recommendation = user.accept(recommendation)

if modify_location is True:
    self.modify_address(new_address)

if modify_distance is True:
    self.modify_distance(new_max_distance)

if modify_time is True:
    self.modify_time(new_time)

if modify_history is True:
    self.modify_history(new_been_to_dic)

if modify_dietary_restriction is True:
    self.modify_dietary_restriction(new_dietary_restriction)

if modify_keywords is True:
    self.modify_keywords(new_keywords)











'''
def retrieve_info(username, user_data):
    
    If the user has an existing account, he can retrieve his been_to_dic and default location data, 
    which automatically show up in the input box
    
    been_to_dic = None
    default_location = None
    with open(user_data, 'r') as user_data:
        reader = csv.reader(user_data, delimtier = ',')
        for row in reader:
            if username == row[0]:
                been_to_dic = row[2]
                default_location = row[1]
    return been_to_dic, default_location
'''
'''
def start(username, location_requirement_dic=None, been_to_dic=None):
    with open(user_data, 'r') as user_data:
        reader = csv.reader(user_data, delimtier = ',')
        for row in reader:
            if username == row[0]:
                been_to_dic = row[2]
                location_requirement_dic = row[1]
    user = User(location_requirement_dic, been_to_dic)
    rec, rec_lst = user.generate_recommendation()
    return rec, rec_lst
    print('restaurant', rec[0])
    print('cuisine', rec[6])
    print('price', rec[7])
    print('rating', rec[3])
    print('distance', rec[4])
'''
    









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
