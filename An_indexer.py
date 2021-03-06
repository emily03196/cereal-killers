import re
import string
import reviews
import json

#Read in Yelp and Google Places data previously stored from API calls



yelp = 'final_yelp_dic.json'
ot_file = 'ot_data.json'



with open(yelp, 'r') as f:
    data = f.read()
yelp_results = json.loads(data)

with open(ot_file, 'r') as f:
    data = f.read()
ot_results = json.loads(data)

with open('big_google.json', 'r') as f:
    data = f.read()
google_results = json.loads(data)

with open('sentiment_dic.json', 'r') as f:
    data = f.read()
sentiment_dic = json.loads(data)




def get_ot_dic():
    '''
    Transform OT dataset from API into dictionary for easy indexing
    '''
    ot_dic = {}
    for call in ot_results:
        ot_dic[call['name']] = call
    return ot_dic



def get_large_index():
    '''
    Build an index that stores for each restaurant: phone  number, rating, cuisine, location(address and coordiantes), price level,
    hours open, and sentiment analysis for the reviews
    '''
    weekday_dic = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

    restaurant_index = {}
    for call in google_results:
        name = call
        if 'permanently_closed' not in google_results[call]:
            restaurant_index[name] = {}
            restaurant_index[name]['price'] = ot_dic[name]['price']
            first = ot_dic[call]['phone'].replace('-', '')
            second = first.replace('x', '')
            phone_no = second[0:10]
            restaurant_index[call]['phone'] = phone_no
            restaurant_index[call]['location'] = {}
            restaurant_index[call]['location']['address'] = ot_dic[call]['address']
            restaurant_index[call]['location']['lat'] = ot_dic[call]['lat']
            restaurant_index[call]['location']['lon'] = ot_dic[call]['lng']
            if 'rating' in google_results[call]:
                restaurant_index[call]['rating'] = google_results[call]['rating']
            if 'error' not in yelp_results[call]: 
                if len(yelp_results[call]['businesses']) != 0:
                    if 'categories' in yelp_results[call]['businesses'][0]:
                        restaurant_index[call]['cuisine'] = [category[0] for category in yelp_results[call]['businesses'][0]['categories']]
            if 'opening_hours' in google_results[call]:
                hours_dic = {}
                periods = google_results[call]['opening_hours']['periods']
                if len(periods) == 1 and 'close' not in periods[0]:
                    for day in weekday_dic:
                        hours_dic[weekday_dic[day]] = ('0000', '2400')
                else:
                    for entry in periods:
                        day = entry['open']['day']
                        hours_dic[weekday_dic[day]] = (entry['open']['time'], entry['close']['time'])
                restaurant_index[call]['hours'] = hours_dic
            if call in sentiment_dic:
                restaurant_index[call]['analyzed_reviews'] = sentiment_dic[call]
            

    return restaurant_index


if __name__ == "__main__":

    ot_dic = get_ot_dic()
    main_index3 = get_large_index()
    
