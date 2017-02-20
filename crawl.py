import bs4
import requests

restaurants = ['Alinea']


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


def get_reviews(restaurants_lst):
    index = {}
    for restaurant in restaurants:
        string = '-'.join(restaurant.lower().split())
        r = requests.get("http://www.yelp.com/biz/"+string+"-chicago?osq=Restaurants")
        c = r.text
        soup = bs4.BeautifulSoup(c, 'html5lib')
        reviews = find_review_words(soup)
        index[restaurant] = reviews
    return index