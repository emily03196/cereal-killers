from django.db import models
from django import forms
from django.http import HttpResponseRedirect 
import datetime

class Username(models.Model):
    username = models.CharField(unique=True, max_length=12, null=True)
    user_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username 

class ResponsesModel(models.Model):
    # http://stackoverflow.com/questions/32423401/save-form-data-in-django
    user= models.OneToOneField(Username, on_delete=models.CASCADE, unique=True)

    diet_choices = [("VT", "Vegetarian"),("VG", "Vegan"), ("HL", "Halal"), ("KS", "Kosher"), ("GF", "Gluten-Free")]
    diet = models.CharField(blank=True, max_length=500, choices=diet_choices) 

    distance = models.IntegerField(blank=True, default=100)

    address = models.CharField(blank=True, max_length=100)

    hurry = models.NullBooleanField(blank=True)

    list_daysofweek = [("MO", "Monday"), ("TU", "Tuesday"), ("WE", "Wednesday"), ("TH", "Thursday"), ("FR", "Friday"), ("SA", "Saturday"), ("SU", "Sunday")]
    arrival_day = models.CharField(blank=True, max_length=10, choices=list_daysofweek)

    now = datetime.datetime.now()
    arrival_time = models.TimeField(editable=True, blank=True, default=now)
    
    def __str__(self):
        return "response_%s" % self.user_id 

class SearchRestaurantsModel(models.Model):
    user= models.OneToOneField(Username, on_delete=models.CASCADE, unique=True)

    search_query1 = models.CharField(max_length=100)
    search_query2 = models.CharField(max_length=100, blank=True)
    search_query3 = models.CharField(max_length=100, blank=True)
    search_query4 = models.CharField(max_length=100, blank=True)
    search_query5 = models.CharField(max_length=100, blank=True)

class PickRestaurantsModel(models.Model):
    user= models.OneToOneField(Username, on_delete=models.CASCADE, unique=True)

    search_results1 = [(None, None)]
    search_results2 = [(None, None)]
    search_results3 = [(None, None)]
    search_results4 = [(None, None)]
    search_results5 = [(None, None)]
    pick_results1 = models.CharField(blank=True, max_length=500, choices=search_results1)
    pick_results2 = models.CharField(blank=True, max_length=500, choices=search_results2)
    pick_results3 = models.CharField(blank=True, max_length=500, choices=search_results3)
    pick_results4 = models.CharField(blank=True, max_length=500, choices=search_results4)
    pick_results5 = models.CharField(blank=True, max_length=500, choices=search_results5)
    rating_choices = [(1,1), (2,2), (3,3), (4,4), (5,5)]
    rating1 = models.CharField(max_length=1, choices=rating_choices, default=5)
    rating2 = models.CharField(max_length=1, choices=rating_choices, default=5)
    rating3 = models.CharField(max_length=1, choices=rating_choices, default=5)
    rating4 = models.CharField(max_length=1, choices=rating_choices, default=5)
    rating5 = models.CharField(max_length=1, choices=rating_choices, default=5)


class RecommendationModel(models.Model):
    user= models.OneToOneField(Username, on_delete=models.CASCADE, unique=True)

    accept = models.NullBooleanField()

class RejectionModel(models.Model):
    user= models.OneToOneField(Username, on_delete=models.CASCADE, unique=True)

    cuisine = models.NullBooleanField(blank=True)
    price_high = models.NullBooleanField(blank=True)
    price_low = models.NullBooleanField(blank=True)

