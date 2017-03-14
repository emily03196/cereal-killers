from django.db import models
from django import forms
from django.http import HttpResponseRedirect 
import datetime
from picklefield.fields import PickledObjectField
from . import COPY_search
import json

data_file = 'pandora/COPY_final_completed_index.json'
with open(data_file, 'r') as f:
    data = f.read()
data_dic = json.loads(data)

class Username(models.Model):
    username = models.CharField(unique=True, max_length=12, null=True)
    user_id = models.AutoField(primary_key=True)
    prev_visited_restaurants = []
    def __str__(self):
        return self.username 

class ResponsesModel(models.Model):
    # http://stackoverflow.com/questions/32423401/save-form-data-in-django
    user= models.OneToOneField(Username, on_delete=models.CASCADE, unique=True)

    diet_choices = [("Vegetarian", "Vegetarian"),("Vegan", "Vegan"), ("Halal", "Halal"), ("Kosher", "Kosher"), ("Gluten-Free", "Gluten-Free")]
    diet = models.CharField(blank=True, max_length=500, choices=diet_choices) 

    distance = models.IntegerField(blank=True, default=100)

    address = models.CharField(blank=True, max_length=100)

    hurry = models.NullBooleanField(blank=True)

    environment = models.NullBooleanField(blank=True)

    service = models.NullBooleanField(blank=True)

    list_daysofweek = [("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"), ("Friday", "Friday"), ("Saturday", "Saturday"), ("Sunday", "Sunday")]
    arrival_day = models.CharField(blank=True, max_length=10, choices=list_daysofweek)

    now = datetime.datetime.now()
    arrival_time = models.TimeField(editable=True, blank=True, default=now)
    
    def __str__(self):
        return "response_%s" % self.user_id 
'''
class SearchRestaurantsModel(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE)
    
    search_query = models.CharField(max_length=100)    

    def __str__(self):
        return self.search_query
    
class SearchChoicesModel(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE)
    search_query_model = models.ForeignKey(SearchRestaurantsModel)
    choice = models.CharField(max_length=200)
    def __str__(self):
        return self.choice
'''
class PickRestaurantsModel(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE)
    #search_choices = models.ManyToManyField(SearchChoicesModel)
    #search_query_model = models.ForeignKey(SearchRestaurantsModel)
    

    #queryset_choices = search_choices.objects.all()
    #list_choices = [(ch, ch) for ch in list(queryset_choices)]

    list_choices = []
    for k, v in data_dic.items():
        list_choices.append(k)
    
    list_choices = sorted(list_choices)
    list_choices = [(ch, ch) for ch in list_choices]

    pick_result = models.CharField(max_length=300, choices=list_choices, default=None)
    
    rating_choices = [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')]
    rating = models.CharField(max_length=1, choices=rating_choices, default=5)
    search_again = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)
    

class RecommendationModel(models.Model):
    user= models.ForeignKey(Username, on_delete=models.CASCADE)

    accept = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)

class RejectionModel(models.Model):
    user= models.ForeignKey(Username, on_delete=models.CASCADE)

    cuisine = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)
    price_high = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)
    price_low = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)

