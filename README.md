# cereal-killers

CS 122 Project - Pandora Restaurant Generator that allows users to input in restaurant history (scoring each restaurant out of 5), price point, distance and time preferences, along with any other specifications. The generator studies the restaurant history and generates the user's preferences based on cuisine types and price range specifications. It will then provide the user with ONE recommendation for a restaurant in Chicago that matches the user's preferences. If the user chooses to reject the suggestion, the generator will continue to recommend restaurants until the user accepts the final recommendation. 


## Files

### Emily_An.py

Make calls to OpenTable, Yelp, and Google Places APIs to obtain data

```
ANY CODE WE HAVE HERE
```

### An_indexer.py

```
ANY CODE WE HAVE HERE
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

```
ANY CODE WE HAVE HERE
```


### Audrey_util.py

```
ANY CODE WE HAVE HERE
```


### search.py

```
ANY CODE WE HAVE HERE
```
## Usage

### Basics

Utilizing the Django module created, we can

```
ANY CODE WE HAVE HERE
```
