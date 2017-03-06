import re
import string
import sys
from collections import Counter


def clean_up_review(review):
    '''
    Review string
    '''
    remove_punctuation = re.compile('[%s]' % re.escape(string.punctuation))
    review = remove_punctuation.sub('', review)
    review_list = review.split(' ')

    review_words_count = Counter(review_list)
    top_words = review_words_count.most_common(3)

    review_pairs_count = Counter(zip(review_list, review_list[1:]))
    top_pairs = review_pairs_count.most_common(3)

# hardcode not important words