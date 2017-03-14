import re
import string
from categories import dietary_choices, service_pos, service_neg, service_p, service_n, waiting_pos, waiting_neg, \
waiting_p, waiting_n, environment_pos, environment_neg, environment_p, environment_n
import sys
import json
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Processes the reviews obtained from the Google Places API and generates a final 
# sentiment dictionary attached to each restaurant that is used in the 
# recommendation algorithm. 

REMOVE_WORDS = ['the', 'a', 'an', 'but', 'if', 'so', 'they', 'them', 'is', 'and', 'to', 'of',\
 'for', 'it', '', 'very', 'their', 'this', 'i', 'my', 'are', 'be', 'was', 'were', 'in', 'as', 'at', \
 'his', 'her', 'she', 'he', 'we', 'you']

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
    review_list = review.replace('\n', '').split(' ')
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

    Waiting score is given a +/-0.33 depending on positive or negative
    review; the sentiment analysis does not properly analyze the waiting set words
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

    Waiting score is given a +/-0.5 depending on positive or negative
    review; the sentiment analysis does not properly analyze the waiting set pairs
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

    sentiment_scores = {}
    
    for restaurant in reviews:
        if len(reviews[restaurant]) != 0:
            sentiment_scores[restaurant] = count_keywords(reviews[restaurant])

    return sentiment_scores
