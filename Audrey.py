from math import radians, cos, sin, asin, sqrt
import json
import Audrey_util



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

been_to_dic = {}
location_requirement_dic = {'user_lat': '40.741895', 'user_long': '-73.989308', 'max_distance':5}
data_file = 'sample_data.json'

with open(data_file, 'r') as f:
    data = f.read()
data = data.replace('\n ', '')
data = data.replace("'", '"')
data_dic = json.loads(data)

def locate(been_to_dic, location_requirement_dic, data_dic):
    user_lat = location_requirement_dic['user_lat'] #string
    user_long = location_requirement_dic['user_long'] #string
    max_distance = location_requirement_dic['max_distance'] #float
    located_restaurants = []
    for restaurant, sub_dic in data_dic.items():
        if restaurant not in been_to_dic:
            lat2 = sub_dic['location']['latitude']
            lat2 = str(lat2)
            lon2 = sub_dic['location']['longitude']
            lon2 = str(lon2)
            miles = Audrey_util.compute_distance(user_lat, user_long, lat2, lon2)
            miles = float(miles)
            if miles <= max_distance:
                located_restaurants.append(restaurant)




def extract_preference(been_to_dic, data_dic):
    cuisine_lst = []
    rating_lst = []
    price_lst =[]
    score_lst = []

    for restaurant, score in been_to_dic.items():
        score_lst.append(score)
        cuisine_lst = cuisine_lst + data_dic[restaurant]['cuisine']
        rating_lst.append(data_dic[restaurant]['rating'])
        price_lst.append(data_dic[restaurant]['price'])











def haversine(lon1, lat1, lon2, lat2):
    '''
    Calculate the circle distance between two points 
    on the earth (specified in decimal degrees)
    '''
    lon1, lat1, lon2, lat2, dlon, dlat = map(radians, [lon1, lat1, lon2, lat2, (lon2-lon1), (lat2-lat1)])
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

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


def calculate_distance(origin, destination):
