from django.db import models
from django import forms
from django.http import HttpResponseRedirect 

class Username(models.Model):
    username = models.CharField(unique=True, max_length=12, null=True)
    user_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username 

class ResponsesModel(models.Model):
    # http://stackoverflow.com/questions/32423401/save-form-data-in-django
    user_id = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)

    diet_choices = [("VT", "Vegetarian"),("VG", "Vegan"), ("HL", "Halal"), ("KS", "Kosher"), ("GF", "Gluten-Free")]
    diet = models.CharField(blank=True, max_length=500, choices=diet_choices) 

    distance = models.IntegerField(blank=True)

    address = models.CharField(blank=True, max_length=100)

    hurry = models.NullBooleanField(blank=True)

    list_daysofweek = [("MO", "Monday"), ("TU", "Tuesday"), ("WE", "Wednesday"), ("TH", "Thursday"), ("FR", "Friday"), ("SA", "Saturday"), ("SU", "Sunday")]
    arrival_day = models.CharField(blank=True, max_length=10, choices=list_daysofweek)

    arrival_time = models.TimeField(editable=True, blank=True, auto_now=True)

class SearchResponsesModel(models.Model):
    search_query1 = models.CharField(max_length=100)
    search_query2 = models.CharField(max_length=100)
    search_query3 = models.CharField(max_length=100)
    search_query4 = models.CharField(max_length=100)
    search_query5 = models.CharField(max_length=100)

class DietRestrictions(models.Model):
    list_choices = [("VT", "Vegetarian"),("VG", "Vegan"), ("HL", "Halal"), ("KS", "Kosher"), ("GF", "Gluten-Free")]
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    choices = models.CharField(blank=True, max_length=500, choices=list_choices) 
    def __str__(self):
        return self.choices

class Distance(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    distance_integer = models.IntegerField(blank=True)
    def __str__(self):
        return self.distance_integer

class Address(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    address_text = models.CharField(blank=True, max_length=100)
    def __str__(self):
        return self.address_text 

class Hurry(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    hurry_choice = models.BooleanField(blank=True)
    def __str__(self):
        return self.hurry_choice 

class Time(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    arrival_time = models.DateTimeField(blank=True, auto_now=True)
    def __str__(self):
        return self.value_to_string(arrival_time)