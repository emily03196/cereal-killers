import re
import string
import reviews
import json

#Read in Yelp and Google Places data previously stored from API calls

reviews_file = 'full_reviews.json'
ph_file = 'google_ph.json'
yelp = 'yelp_data.json'


with open(reviews_file, 'r') as f:
    data = f.read()
reviews_index = json.loads(data)

for restaurant in reviews_index:
    re = reviews_index[restaurant]
    for review in re:
        review = review.replace('\n', '')


with open(ph_file, 'r') as f:
    data = f.read()
ph_index = json.loads(data)

with open(yelp, 'r') as f:
    data = f.read()
yelp_results = json.loads(data)

def parse_reviews():
    '''
    Parse reviews and count keywords to address user's specific requirements
    '''
    parsed = {}
    for restaurant in reviews_index:
        parsed[restaurant] = reviews.count_keywords(reviews_index[restaurant])
    return parsed



def get_large_index(parsed_reviews, ph_index, yelp_results):
    '''
    Build an index that stores for each restaurant: phone  number, rating, cuisine, location(address and coordiantes), price level,
    hours open, and word counts from the reivews
    '''
    weekday_dic = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

    restaurant_index = {}

    for call in yelp_results:
        if 'error' not in call:
            restaurants = call['businesses']
            for restaurant in restaurants:
                if restaurant['is_closed'] == False:
                    restaurant_name = restaurant['name']
                    restaurant_index[restaurant_name] = {}
                    restaurant_index[restaurant_name]['rating'] = restaurant['rating']
                    restaurant_index[restaurant_name]['phone'] = restaurant['display_phone']
                    if 'categories' in restaurant:
                        restaurant_index[restaurant_name]['cuisine'] = [category[0] for category in restaurant['categories']]
                    restaurant_index[restaurant_name]['location'] = {}
                    if len(restaurant['location']['address']) > 0:
                        restaurant_index[restaurant_name]['location']['address'] = restaurant['location']['address'][0]
                        restaurant_index[restaurant_name]['location']['latitude'] = restaurant['location']['coordinate']['latitude']
                        restaurant_index[restaurant_name]['location']['longitude'] = restaurant['location']['coordinate']['longitude']
                    if restaurant_name in ph_index:
                        if 'price' in ph_index[restaurant_name]:
                            restaurant_index[restaurant_name]['price'] = ph_index[restaurant_name]['price']
                        if 'hours' in ph_index[restaurant_name]:
                            hours_dic = {}
                            periods = ph_index[restaurant_name]['hours']['periods']
                            for entry in periods:
                                day = entry['open']['day']
                                if 'close' in entry:
                                    hours_dic[weekday_dic[day]] = (entry['open']['time'], entry['close']['time'])
                                
                            restaurant_index[restaurant_name] = hours_dic
                    if restaurant_name in parsed_reviews:
                        restaurant_index[restaurant_name]['parsed_reviews'] = parsed_reviews[restaurant_name]
                  

    return restaurant_index


if __name__ == "__main__":
    
    parsed_reviews = parse_reviews()
    main_index = get_large_index(parsed_reviews, ph_index, yelp_results)