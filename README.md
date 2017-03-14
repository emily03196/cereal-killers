# cereal-killers

CS 122 Project - Pandora Restaurant Generator that allows users to input in restaurant history (scoring each restaurant out of 5), price point, distance and time preferences, along with any other specifications. The generator studies the restaurant history and generates the user's preferences based on cuisine types and price range specifications. It will then provide the user with ONE recommendation for a restaurant in Chicago that matches the user's preferences. If the user chooses to reject the suggestion, the generator will continue to recommend restaurants until the user accepts the final recommendation. 


## Files

### Emily_An.py

Make calls to OpenTable, Yelp, and Google Places APIs to obtain data

```
ANY CODE WE HAVE HERE
```

### An_indexer.py

Reads in Yelp and Google Places data previously stored from API calls
```
ANY CODE WE HAVE HERE
```

### categories.py
Used to obtain lists of positive and negative words for the individual categories of service, wait time, and environment, along with a list of dietary choices to be used in the final sentiment dictionary. 

For example:
```
waiting_pos = ['fast', 'quick', 'short', 'immediate']
waiting_neg = ['long', 'slow', 'busy', 'wait', 'packed']
waiting = ['time', 'wait', 'waited']
```

### reviews.py
References "categories.py" to parse through reviews from the Google Place Search API and determines a final sentiment dictionary for each individual restaurant. 

Example review data:
```
{
  ‘Umi’: ['Amazing sushi! Very fresh and super tasty. I love their philly and miami options. Staff is very friendly and great
  environment to dine in.', 
  ‘Some of the best ramen I've had so far in Chicago, and I'm something of a ramen snob. Great, friendly service, nice decor, good
  sushi. Never had to wait for a table. Ice cold Sapporo. Convenient parking. Reasonable prices. What more can I say? I think the place   is great.  I will be a regular...’
}
```

Example sentiment dictionary output:
```
{
 'The Portage': 
    {'dietary_choices': [vegetarian],  
     'environment_score': 0.12498000000000001,  
     'service_score': 0.04213999999999999,  
     'waiting_score': -0.16599999999999998}, 
 'The Publican': 
    {'dietary_choices': [allergy],  
    'environment_score': 0.0,  
    'service_score': 0.09878,  
    'waiting_score': -0.198}, 
 'The Rosebud': 
    {'dietary_choices': [],  
    'environment_score': 0.16514,  
    'service_score': 0.12498000000000001,  
    'waiting_score': -0.066}, 
 'The Savoy': 
    {'dietary_choices': [],  
    'environment_score': 0.0,  
    'service_score': 0.41717999999999994,  
    'waiting_score': -0.066}
}
```

### Audrey_user.py
Generates the overall recommendation for the restaurant based on user history to generate the user's individual cuisine preferences. The algorithm then locates potential restaurants that match the user's specifications for distance from, hours to, and scores each of the restaurants based on these requirements. The algorithm then outputs a final restaurant as the recommendation. 

Example input into the algorithm:
```
been_to_dic = {'Yusho': 4, 'bellyQ': 3, 'Chicago Peoples Temple': 5, 'Dine': 4}
address = '6031 South Ellis Ave'
max_distance = 20
dietary_restriction = ['Vegetarian']
time = 'Monday 1800'
username = 'Liz'
keywords = {'environment': None, 'service': None, 'waiting': None}
```
Example output:
```
ANY CODE WE HAVE HERE
```

If the restaurant is rejected, we input:
```
ANY CODE WE HAVE HERE
```
and the restaurant generates a new recommendation until we accept the final recommendation. 


### search.py

```
ANY CODE WE HAVE HERE
```
## Usage

### Django Module

Separate forms created for the Django module:
#### LoginForm: 
```
model = Username
fields = ["username", 'user_id']
```

#### ResponseForm:
```
model = ResponsesModel
fields = ['diet', 'distance', 'address', 'hurry', 'arrival_day', 'arrival_time']
```

#### SearchRestaurantsForm
```
model = SearchRestaurantsModel
fields = ['search_query1', 'search_query2', 'search_query3', 'search_query4', 'search_query5']
```

#### PickRestaurantsForm:
```
model = PickRestaurantsModel
fields = ['pick_results1', 'pick_results2', 'pick_results3', 'pick_results4', 'pick_results5']
```

#### RecommendationForm:
```
model = RecommendationModel
fields = ['accept']
```

#### RejectionForm:
```
model = RejectionModel
fields = ["cuisine", "price_high", "price_low"]
```
