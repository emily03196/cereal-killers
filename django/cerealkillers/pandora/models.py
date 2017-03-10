from django.db import models
from django import forms
from django.http import HttpResponseRedirect 

class Username(models.Model):
    user_text = models.CharField(max_length=12, null=True)    
    def __str__(self):
        return self.user_text 

class DietRestrictions(models.Model):
    list_choices = [("VT", "Vegetarian"),("VG", "Vegan"), ("HL", "Halal"), ("KS", "Kosher"), ("GF", "Gluten-Free")]
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    choices = models.CharField(max_length=500, choices=list_choices) 
    def __str__(self):
        return self.choices

class Distance(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    distance_integer = models.IntegerField()
    def __str__(self):
        return self.distance_integer

class Address(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    address_text = models.CharField(max_length=100)
    def __str__(self):
        return self.address_text 

class Hurry(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    hurry_choice = models.BooleanField()
    def __str__(self):
        return self.hurry_choice 

class Time(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, default=None)
    arrival_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.value_to_string(arrival_time)


# class Question(models.Model):
#     question_text = models.CharField(max_length=500)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text

# class DropdownChoice(models.Model):
# https://docs.djangoproject.com/en/dev/ref/forms/fields/#choicefield