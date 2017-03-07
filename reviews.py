import re
import string
import sys
from collections import Counter

REMOVE_WORDS = ['the', 'a', 'an', 'but', 'if', 'so', 'they', 'them', 'is', 'and', 'to', 'of',\
 'for', 'it', '', 'very', 'their', 'this', 'i', 'my', 'are']

def clean_up_review(reviews):
    '''
    List of review strings
    '''
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