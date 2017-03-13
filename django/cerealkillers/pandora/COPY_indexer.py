import re
import requests
import urllib
import util
import bs4
import queue
import sys
import json
from collections import deque


def indexer(index, restaurant):
	'''
	
	'''
	info = get_restaurant_info(restaurant)
	name = info['restaurant_name'] 
	review_info = find_review_words(restaurant)
	price_bounds = re.findall('\d+', info['price_range'])
	price_bounds_int = []
	
	for i in price_bounds:
		price_bounds_int.append(int(i))

	price_bounds_int = tuple(price_bounds_int)

    index[name] = {}
    index[name['cuisine']] = info['cuisine']
    index[name['address']] = info['address']
    index[name['average_rating']] = info['average_rating']
    index[name['price_range']] = price_bounds_int
    index[name['reviews']] = review_info


def find_review_words(restaurant):
    '''
    Finds words within individual reviews
    '''
    all_reviews = restaurant.find_all('div', itemprop = "review")

    for review in all_reviews:
        review = review.text.replace('\n', ' ')
        keywords = review.split(' ')
        keywords = [word for word in keywords if word != '']

    return keywords


def get_restaurant_info(restaurant):
    '''
    Obtains information pertaining to each individual restaurant
    '''
    top_reviews = restaurant.find_all('script', type="application/ld+json")[0].string
    top_reviews = json.loads(top_reviews)

    restaurant_name = top_reviews['name']
    price_range = top_reviews['priceRange']
    address = top_reviews['address']['streetAddress']
    average_rating = top_reviews['aggregateRating']['ratingValue']
    cuisine = top_reviews['servesCuisine']

    rv = {}
    rv['restaurant_name'] = restaurant_name
    rv['price_range'] = price_range
    rv['address'] = address
    rv['average_rating'] = average_rating
    rv['cuisine'] = cuisine

    return rv