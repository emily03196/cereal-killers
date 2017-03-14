# Used to obtain lists of positive and negative words for the individual categories of 
# service, wait time, and environment, along with list of dietary choices to be used 
# in the final sentiment dictionary. 


# Modifiers
positive_words = ['good', 'best', 'great', 'outstanding', 'excellent', 'amazing', 'spectacular', \
    'wonderful', 'magnificent', 'awesome', 'perfect', 'phenomenal', 'cool', 'favorite', 'fantastic', \
    'fun', 'great', 'delightful', 'nice', 'love', 'loved', 'outstanding', 'lovely']

negative_words = ['bad', 'worst', 'mediocre', 'horrible', 'terrible', 'sad', 'disappointing']


# Dietary Restrictions
dietary_choices = ['vegetarian', 'vegan', 'gluten-free', 'halal', 'kosher', 'paleo', 'allergies', 'allergy']


# Service Related 
service_pos = ['friendly', 'courteous', 'accommodating', 'professional', 'attentive', 'delight', \
    'helpful', 'passionate', 'welcoming', 'efficient', 'kind', 'fast', 'quick', 'immediate', 'impeccable']
service_neg = ['disregard', 'ignored', 'rude', 'mess', 'mean', 'slow'] 
service = ['service', 'waiter', 'waitress', 'staff', 'server']

service_p = [word + ' ' + serv for word in positive_words for serv in service] + \
    [serv + ' ' + word for word in positive_words for serv in service]
service_n = [word + ' ' + serv for word in negative_words for serv in service] + \
    [serv + ' ' + word for word in negative_words for serv in service]


# Wait Time Related
waiting_pos = ['fast', 'quick', 'short', 'immediate']
waiting_neg = ['long', 'slow', 'busy', 'wait', 'packed']
waiting = ['time', 'wait', 'waited']

waiting_p = [word + ' ' + wait for word in waiting_pos for wait in waiting] + \
    [wait + ' ' + word for word in waiting_pos for wait in waiting]
waiting_n = [word + ' ' + wait for word in waiting_neg for wait in waiting] + \
    [wait + ' ' + word for word in waiting_neg for wait in waiting]


# Environment 
environment_pos = ['warm', 'trendy', 'stylish', 'inviting', 'cozy', 'intimate', 'charming', 'bright', 'cute', \
'clean', 'classy']
environment_neg = ['cold', 'chilly', 'dirty', 'noisy', 'ugly']
environment = ['ambience', 'ambiance', 'atmosphere', 'decor', 'decoration', 'vibe', 'location', 'interior', \
'views', 'experience', 'space', 'inside', 'spot', 'environment', 'place']

environment_p = [word + ' ' + env for word in positive_words for env in environment] + \
    [env + ' ' + word for word in positive_words for env in environment]
environment_n = [word + ' ' + env for word in negative_words for env in environment] + \
    [env + ' ' + word for word in negative_words for env in environment]
