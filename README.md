# cereal-killers

CS 122 Project - Pandora Restaurant Generator that allows users to input in restaurant history (scoring each restaurant out of 5), price point, distance and time preferences, along with any other specifications. The generator studies the restaurant history and generates the user's preferences based on cuisine types and price range specifications. It will then provide the user with ONE recommendation for a restaurant in Chicago that matches the user's preferences. If the user chooses to reject the suggestion, the generator will continue to recommend restaurants until the user accepts the final recommendation. 


## Files

### Emily_An.py

Make calls to OpenTable, Yelp, and Google Places APIs to obtain data

Sample data:
```
#Sample OpenTable data:
[...{"area": "Chicago / Illinois", "address": "330 N State Street", "state": "IL", "lng": -87.628091, "postal_code": "60610", "city": "Chicago", "reserve_url": "http://www.opentable.com/single.aspx?rid=7267", "image_url": "https://www.opentable.com/img/restimages/7267.jpg", "name": "10pin Bowling Lounge", "price": 4, "mobile_reserve_url": "http://mobile.opentable.com/opentable/?restId=7267", "id": 7267, "country": "US", "phone": "3126440300x", "lat": 41.888634}, {"area": "Chicago / Illinois", "address": "60 W Ontario St", "state": "IL", "lng": -87.63045, "postal_code": "60654", "city": "Chicago", "reserve_url": "http://www.opentable.com/single.aspx?rid=147604", "image_url": "https://www.opentable.com/img/restimages/147604.jpg", "name": "Chicago Chop House", "price": 4, "mobile_reserve_url": "http://mobile.opentable.com/opentable/?restId=147604", "id": 147604, "country": "US", "phone": "3127877100", "lat": 41.893491}, {"area": "Chicago / Illinois", "address": "2824 West Armitage Avenue", "state": "IL", "lng": -87.698281, "postal_code": "60647", "city": "Chicago", "reserve_url": "http://www.opentable.com/single.aspx?rid=149062", "image_url": "https://www.opentable.com/img/restimages/149062.jpg", "name": "Osteria Langhe", "price": 2, "mobile_reserve_url": "http://mobile.opentable.com/opentable/?restId=149062", "id": 149062, "country": "US", "phone": "7736611582x", "lat": 41.917688}, {"area": "Chicago / Illinois", "address": "633 North Saint Clair", "state": "IL", "lng": -87.622615, "postal_code": "60611", "city": "Chicago", "reserve_url": "http://www.opentable.com/single.aspx?rid=2053", "image_url": "https://www.opentable.com/img/restimages/2053.jpg", "name": "The Capital Grille - Chicago - Downtown", "price": 4, "mobile_reserve_url": "http://mobile.opentable.com/opentable/?restId=2053", "id": 2053, "country": "US", "phone": "3123379400x", "lat": 41.893591}...]

#Sample Google data:
{..."Rivers": {"opening_hours": {"periods": [{"open": {"time": "1130", "day": 1}, "close": {"time": "2100", "day": 1}}, {"open": {"time": "1130", "day": 2}, "close": {"time": "2100", "day": 2}}, {"open": {"time": "1130", "day": 3}, "close": {"time": "2100", "day": 3}}, {"open": {"time": "1130", "day": 4}, "close": {"time": "2100", "day": 4}}, {"open": {"time": "1130", "day": 5}, "close": {"time": "2200", "day": 5}}, {"open": {"time": "1700", "day": 6}, "close": {"time": "2200", "day": 6}}], "weekday_text": ["Monday: 11:30 AM \u2013 9:00 PM", "Tuesday: 11:30 AM \u2013 9:00 PM", "Wednesday: 11:30 AM \u2013 9:00 PM", "Thursday: 11:30 AM \u2013 9:00 PM", "Friday: 11:30 AM \u2013 10:00 PM", "Saturday: 5:00 \u2013 10:00 PM", "Sunday: Closed"], "open_now": false, "exceptional_date": []}, "formatted_phone_number": "(312) 984-1718", "reference": "CmRSAAAA-EQYNPNQZsg5oBheKCjIZB5UZQP7tmuLZG9e03i8BfxjtoWfSeu8UZOEPEmY88OjpKIdEK78bHFmDEvIzEoVIYH3cNIa3AIw1Qn3hJIF14XVZJEpQSLBaeiTpjVLHLC_EhDpKsP-IXJPM5gHyRAtjvYzGhSfO-25H7WgTNsJFmt3g-eBpi1WJA", "url": "https://maps.google.com/?cid=16598770869000221617", "website": "http://www.trattoriaten.com/", "adr_address": "<span class=\"street-address\">10 N Dearborn St #1</span>, <span class=\"locality\">Chicago</span>, <span class=\"region\">IL</span> <span class=\"postal-code\">60602</span>, <span class=\"country-name\">USA</span>", "reviews": [{"text": "I had been there several years ago and had very fond memories of the place.  The food was excellent, especially the ravioli, but nothing that knocks your socks off. What was really amazing was the bourbon cocktail I had with delicious coffee and chocolate flavors. The service was a bit on the slow side initially in getting us seated and taking orders, but then it picked up. A good Italian option in the loop.", "rating": 4, "profile_photo_url": "//lh4.googleusercontent.com/-2LS1Wov0wb4/AAAAAAAAAAI/AAAAAAABRTA/UhgNmwo_yoA/s128/photo.jpg", "aspects": [{"type": "overall", "rating": 2}], "author_url": "https://www.google.com/maps/contrib/110063128841143711459/reviews", "time": 1485989467, "language": "en", "author_name": "Vinod Kalathil", "relative_time_description": "a month ago"}, {"text": "I don't often partake in finer dining, so maybe that's the reason I was blown away. Regardless, the food was great and the waitstaff were friendly, helpful, and personable. The veal and the quail were very good, as was the squid ink pasta and the ravioli. The atmosphere is somewhat unique and worked well for a date with a special someone.", "rating": 5, "profile_photo_url": "//lh5.googleusercontent.com/-0Ze1OSrgjws/AAAAAAAAAAI/AAAAAAAAADE/dwdWvgnzyAQ/s128/photo.jpg", "aspects": [{"type": "overall", "rating": 3}], "author_url": "https://www.google.com/maps/contrib/114165726899490169791/reviews", "time": 1484685426, "language": "en", "author_name": "Chase Yoder", "relative_time_description": "a month ago"}, {"text": "Visited for lunch yesterday. Was impressed by the very nice and relaxing atmosphere. I ordered from the restaurant week 3 course menu. Each dish was phenomenal. In fact, the experience was so good I went back today. Highly recommended.", "rating": 5, "profile_photo_url": "//lh6.googleusercontent.com/-72lJ2yStmRI/AAAAAAAAAAI/AAAAAAAAAkM/qfDcMjs40wo/s128/photo.jpg", "aspects": [{"type": "overall", "rating": 3}], "author_url": "https://www.google.com/maps/contrib/100227552023739622946/reviews", "time": 1485914457, "language": "en", "author_name": "Brent Reame", "relative_time_description": "a month ago"}, {"text": "You will savor every bite. I tried the Butternut and Acorn Squash Ravioli, Pan Roasted Sustainable Lake Superior Whitefish, and Chocolate Truffle Cake, words cannot describe... It was excellent, as well as the venue (it is beautiful) and the staff. Worth It.", "rating": 5, "profile_photo_url": "//lh5.googleusercontent.com/-go31UC0_RkU/AAAAAAAAAAI/AAAAAAAAAAA/AAomvV2Pjhfcv-7p_J2MIAhCZ2AWo6OW4w/s128/photo.jpg", "aspects": [{"type": "overall", "rating": 3}], "author_url": "https://www.google.com/maps/contrib/108023970774271530034/reviews", "time": 1486670997, "language": "en", "author_name": "JaimeL", "relative_time_description": "3 weeks ago"}, {"text": "How did I not know about this place sooner?! Ambiance, food, and service were all perfect.  Pasta's were spot on and the gnocchi melts in your mouth.  My new favorite place for Italian food.", "rating": 5, "profile_photo_url": "//lh6.googleusercontent.com/-WDeEzJ7fvBg/AAAAAAAAAAI/AAAAAAAAAI0/EiZT-VgNYIk/s128/photo.jpg", "aspects": [{"type": "overall", "rating": 3}], "author_url": "https://www.google.com/maps/contrib/115671186143216884621/reviews", "time": 1485811835, "language": "en", "author_name": "Ben Seiber", "relative_time_description": "a month ago"}], "types": ["bar", "restaurant", "food", "point_of_interest", "establishment"]...}

#Sample Yelp data:
{"Rivers": {"total": 1, "region": null, "businesses": [{"review_count": 268, "rating": 3.5, "phone": "+13125591515", "display_phone": "+1-312-559-1515", "rating_img_url_small": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/2e909d5d3536/ico/stars/v1/stars_small_3_half.png", "url": "https://www.yelp.com/biz/rivers-chicago?adjust_creative=MTzuVjKQZCEcQAqcJR4PuA&utm_campaign=yelp_api&utm_medium=api_v2_phone_search&utm_source=MTzuVjKQZCEcQAqcJR4PuA", "menu_date_updated": 1472582290, "is_closed": false, "is_claimed": true, "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/FAxHqoiQb_oZXQmqqcJTUQ/ms.jpg", "name": "Rivers", "categories": [["American (New)", "newamerican"], ["Seafood", "seafood"]], "menu_provider": "single_platform", "mobile_url": "https://m.yelp.com/biz/rivers-chicago?adjust_creative=MTzuVjKQZCEcQAqcJR4PuA&utm_campaign=yelp_api&utm_medium=api_v2_phone_search&utm_source=MTzuVjKQZCEcQAqcJR4PuA", "id": "rivers-chicago", "snippet_text": "Food is great and the presentation is superb. What makes this restaurant unique is the view... breathtaking riverwalk view! \nA bit difficult finding the...", "location": {"geo_accuracy": 9.5, "cross_streets": "Madison St & Arcade Pl", "postal_code": "60606", "address": ["30 S Wacker Dr"], "display_address": ["30 S Wacker Dr", "The Loop", "Chicago, IL 60606"], "city": "Chicago", "coordinate": {"latitude": 41.8812346688533, "longitude": -87.6375108823615}, "neighborhoods": ["The Loop"], "state_code": "IL", "country_code": "US"}, "snippet_image_url": "https://s3-media1.fl.yelpcdn.com/photo/GN_pwT3XF8T1AU9WsWY8yQ/ms.jpg", "rating_img_url": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/5ef3eb3cb162/ico/stars/v1/stars_3_half.png", "rating_img_url_large": "https://s3-media3.fl.yelpcdn.com/assets/2/www/img/bd9b7a815d1b/ico/stars/v1/stars_large_3_half.png"}]}, "Bistro Dre": {"total": 1, "region": null, "businesses": [{"review_count": 311, "rating": 3.5, "phone": "+17736979067", "display_phone": "+1-773-697-9067", "rating_img_url_small": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/2e909d5d3536/ico/stars/v1/stars_small_3_half.png", "url": "https://www.yelp.com/biz/bistro-dre-chicago?adjust_creative=MTzuVjKQZCEcQAqcJR4PuA&utm_campaign=yelp_api&utm_medium=api_v2_phone_search&utm_source=MTzuVjKQZCEcQAqcJR4PuA", "menu_date_updated": 1472765005, "is_closed": true, "is_claimed": false, "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/3sObvxUx0HEcmmROMHr-SA/ms.jpg"...}
```

### An_indexer.py

Reads in Yelp and Google Places data previously stored from API calls

Sample index entry:
```
main_index3 = {"Rivers": {"cuisine": ["American (New)", "Seafood"], "rating": 4.4, "phone": "3125591515", "url": "https://maps.google.com/?cid=16598770869000221617", "image_url": "https://www.opentable.com/img/restimages/3583.jpg", "price": 2, "hours": {"Friday": ["1130", "2200"], "Saturday": ["1700", "2200"], "Tuesday": ["1130", "2100"], "Monday": ["1130", "2100"], "Thursday": ["1130", "2100"], "Wednesday": ["1130", "2100"]}, "location": {"address": "10 & 30 South Wacker Drive", "lon": -87.6369, "lat": 41.8815}, "analyzed_reviews": {"dietary_choices": [], "service_score": 0.18308, "waiting_score": -0.066, "environment_score": 0.0}}...}

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
