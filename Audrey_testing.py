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
    for restaurant in data_dic:
        if restaurant not in been_to_dic:
            lat2 = 
            miles = Audrey_util.compute_distance(user_lat, user_long, str(restaurant['location']['latitude']), str(restaurant['location']['longitude'])
            if miles <= max_distance:
                located_restaurants.append(restaurant)
    return located_restaurants
