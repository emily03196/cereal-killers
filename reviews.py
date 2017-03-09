import re
import string
import sys
import json
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

REMOVE_WORDS = ['the', 'a', 'an', 'but', 'if', 'so', 'they', 'them', 'is', 'and', 'to', 'of',\
 'for', 'it', '', 'very', 'their', 'this', 'i', 'my', 'are', 'be', 'was', 'were', 'in', 'as']

# Modifiers
positive_words = ['good', 'best', 'great', 'outstanding', 'excellent', 'amazing', 'spectacular', \
    'wonderful', 'magnificent', 'awesome', 'perfect', 'phenomenal', 'cool', 'favorite', 'fantastic', \
    'fun', 'great', 'delightful', 'nice', 'love', 'loved']

negative_words = ['bad', 'worst', 'mediocre', 'horrible', 'terrible', 'sad', 'disappointing']


# Dietary Restrictions
dietary_choices = ['vegetarian', 'vegan', 'gluten-free', 'halal', 'kosher', 'paleo', 'allergies', 'allergy']


# Service Related 
service_pos = ['friendly', 'courteous', 'accommodating', 'professional', 'attentive', \
    'helpful', 'passionate', 'welcoming', 'efficient', 'kind', 'fast', 'quick', 'immediate']
service_neg = ['disregard', 'ignored', 'rude', 'mess', 'mean', 'slow'] 
service = ['service', 'waiter', 'waitress', 'staff']

service_p = [word + ' ' + serv for word in positive_words for serv in service] + \
    [serv + ' ' + word for word in positive_words for serv in service]
service_n = [word + ' ' + serv for word in negative_words for serv in service] + \
    [serv + ' ' + word for word in negative_words for serv in service]


# Wait Time Related
waiting_pos = ['fast', 'quick', 'short', 'immediate']
waiting_neg = ['long', 'slow', 'busy', 'wait']
waiting = ['time', 'wait', 'waited']

waiting_p = [word + ' ' + wait for word in waiting_pos for wait in waiting] + \
    [wait + ' ' + word for word in waiting_pos for wait in waiting]
waiting_n = [word + ' ' + wait for word in waiting_neg for wait in waiting] + \
    [wait + ' ' + word for word in waiting_neg for wait in waiting]


# Environment 
environment_pos = ['warm', 'trendy', 'stylish', 'inviting', 'cozy', 'intimate']
environment_neg = ['cold', 'chilly', 'dirty', 'noisy', 'ugly']
environment = ['ambience', 'atmosphere', 'decor', 'decoration', 'vibe', 'location', 'interior', 'views']

environment_p = [word + ' ' + env for word in positive_words for env in environment] + \
    [env + ' ' + word for word in positive_words for env in environment]
environment_n = [word + ' ' + env for word in negative_words for env in environment] + \
    [env + ' ' + word for word in negative_words for env in environment]


def find_sentiment(words):
    '''
    Hutto, C.J. & Gilbert, E.E. (2014). 
    VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. 
    Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

    Determines sentiment of words (string) input via NLTK's Vader SentimentIntensityAnalyzer
    '''
    sentiment_score = 0

    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(words)
    sentiment_score = sentiment_score + ss['compound']

    return sentiment_score


def cleanup_reviews(review):
    '''
    Returns list of unique words and combinations of pairs from review string
    '''
    remove_punctuation = re.compile('[%s\d]' % re.escape(string.punctuation))
    review = remove_punctuation.sub('', review).lower()
    review_list = review.split(' ')
    review_list = [word for word in review_list if word not in REMOVE_WORDS]
    review_words = list(set(review_list))

    review_pairs_count = Counter(zip(review_list, review_list[1:]))
    pairs = review_pairs_count.most_common()
    pairs = sorted(pairs, key=lambda x: x[1], reverse = True)
    word_pairs = [pair[0][0] + ' ' + pair[0][1] for pair in pairs]

    return review_words, word_pairs


def keyword_analysis(word):
    '''
    Determines sentiment of string input based on categorization
    '''
    service_score = 0
    waiting_score = 0
    environment_score = 0
    
    if word in service_pos:
        service_score += find_sentiment(word)
    elif word in service_neg:
        service_score += find_sentiment(word)
    if word in waiting_pos:
        waiting_score += 0.33
    elif word in waiting_neg:
        waiting_score += -0.33
    if word in environment_pos:
        environment_score += find_sentiment(word)
    elif word in environment_neg:
        environment_score += find_sentiment(word)

    return (service_score, waiting_score, environment_score)


def keypair_analysis(pair):
    '''
    Determines sentiment of string input based on categorization
    '''
    service_score = 0
    waiting_score = 0
    environment_score = 0
    
    if pair in service_p:
        service_score += find_sentiment(pair)
    elif pair in service_n:
        service_score += find_sentiment(pair)
    if pair in waiting_p:
        waiting_score += 0.5
    elif pair in waiting_n:
        waiting_score += -0.5
    if pair in environment_p:
        environment_score += find_sentiment(pair)
    elif pair in environment_n:
        environment_score += find_sentiment(pair)

    return (service_score, waiting_score, environment_score)


def count_keywords(reviews):
    '''
    Determines dietary restrictions and individual scores for service, 
    waiting, and environment based on review strings
    '''
    dietary_concerns = set()
    service_score = 0
    waiting_score = 0
    environment_score = 0

    for review in reviews:
        review_words, word_pairs = cleanup_reviews(review)
        for word in review_words:
            if word in dietary_choices:
                dietary_concerns.add(word)
            scores_words = keyword_analysis(word)
            service_score += scores_words[0]
            waiting_score += scores_words[1]
            environment_score += scores_words[2]
        for pair in word_pairs:
            scores_pairs = keypair_analysis(pair)
            service_score += scores_pairs[0]
            waiting_score += scores_pairs[1]
            environment_score += scores_pairs[2]

    return {'dietary_choices': list(dietary_concerns), 'service_score': service_score / len(reviews), \
    'waiting_score': waiting_score / len(reviews), 'environment_score': environment_score / len(reviews)}


def determine_sentiment(json_filename):
    '''
    Assigns score dictionary to each individual restaurant based on json file
    '''
    with open(json_filename) as reviews_file:    
        reviews = json.load(reviews_file)
    for restaurant in reviews:
        re = reviews[restaurant]
    for review in re:
        review = review.replace('\n', '')

    sentiment_scores = {}
    
    for restaurant in reviews:
        if len(reviews[restaurant]) != 0:
            sentiment_scores[restaurant] = count_keywords(reviews[restaurant])

    return sentiment_scores