import re
import string
import reviews
import json

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

def parse_reviews():
    parsed = {}
    for restaurant in reviews_index:
        parsed[restaurant] = reviews.count_keywords(reviews_index[restaurant])
    return parsed


def get_large_index(parsed_reviews, ph_index, yelp_results):
    '''
    restaurant index from multiple yelp api calls and ot data 
    '''

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
                            restaurant_index[restaurant_name]['hours'] = ph_index[restaurant_name]['hours']['periods']
                    if restaurant_name in parsed_reviews:
                        restaurant_index[restaurant_name]['parsed_reviews'] = parsed_reviews[restaurant_name]
                  
    
    return restaurant_index


if __name__ == "__main__":
    
    parsed_reviews = parse_reviews()
    main_index = get_large_index(parsed_reviews, ph_index, yelp_results)

main_index = get_large_index(parsed_reviews, ph_index, yelp_results)
