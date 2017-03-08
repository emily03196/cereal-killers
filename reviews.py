import re
import string
import sys
from collections import Counter

REMOVE_WORDS = ['the', 'a', 'an', 'but', 'if', 'so', 'they', 'them', 'is', 'and', 'to', 'of',\
 'for', 'it', '', 'very', 'their', 'this', 'i', 'my', 'are']

dietary_choices = ['vegetarian', 'vegan', 'gluten-free', 'halal', 'kosher']

positive_words = ['good', 'best', 'great', 'outstanding', 'excellent', 'amazing', 'spectacular', \
'wonderful', 'magnificent', 'awesome', 'perfect']
negative_words = ['bad', 'worst', 'mediocre', 'horrible', 'terrible']

#Service
#positive
service_p = ['friendly', 'courteous', 'accommodating', 'professional', 'attentive', 'delightful', \
'helpful', 'passionate', 'welcoming', 'efficient', 'kind']
service_p = service_p + [word+' service' for word in positive_words] + \
[word+' waiter' for word in positive_words] + [word+' waitress' for word in positive_words]
#negative
service_n = ['disregard', 'ignore', 'rude', 'mess'] 
service_n = service_n + [word+' service' for word in negative_words] + \
[word+' waiter' for word in negative_words] + [word+' waitress' for word in negative_words]

#Waiting time
waiting_p = ['fast', 'quick']
waiting_n = [' wait ', 'waited', 'long', 'slow', 'busy']

#Environment
environment = ['ambience', 'atmosphere', 'decor', 'decoration', 'vibe', 'trendy', 'inviting', 'warm']

def count_keywords(reviews):
    dietary_dic = {}
    service_score = 0
    waiting_score = 0
    music = 0
    sight = 0
    environment = 0
    for review in reviews:
        for dietary_choice in dietary_choices:
            if dietary_choice in review:
                dietary_dic[dietary_choice] = dietary_dic.get(dietary_choice, 0) + 1
        if any(word in review for word in service_p):
            service_score += 1
        if any(word in review for word in service_n):
            service_score -= 1
        if any(word in review for word in waiting_p):
            waiting_score += 1
        if any(word in review for word in waiting_n):
            waiting_score -= 1
        if 'music' in review:
            music += 1
        if 'sight' in review:
            sight += 1
        if any(word in review for word in environment):
            environment += 1

    return {'dietary_restriction': dietary_dic, 'service_score': service_score, \
    'waiting_score': waiting_score, 'music': music, 'sight': sight, 'environment': environment}

'''
def clean_up_review(reviews):
    
    List of review strings
    
    for review in reviews:
        remove_punctuation = re.compile('[%s\d]' % re.escape(string.punctuation))
        review = remove_punctuation.sub('', review).lower()
        review_list = review.split(' ')
        review_list = [word for word in review_list if word not in REMOVE_WORDS]

        review_words_count = Counter(review_list)
        words = review_words_count.most_common(5)
        top_words = [words[i] for i in range(len(words))]
        top_words = sorted(top_words, key=lambda x: x[1], reverse = True)

        review_pairs_count = Counter(zip(review_list, review_list[1:]))
        pairs = review_pairs_count.most_common(20)
        top_pairs = [pairs[i] for i in range(len(pairs))]
        top_pairs = sorted(top_pairs, key=lambda x: x[1], reverse = True)

    return top_words, top_pairs
'''