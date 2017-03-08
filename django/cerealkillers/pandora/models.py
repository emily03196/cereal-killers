from django.db import models
from django import forms

class Username(models.Model):
    username = forms.CharField(max_length=12, min_length=6)
    def __str__(self):
        return self.username 

class DietRestrictions(models.Model):
    list_choices = [("VT", "Vegetarian"),("VG", "Vegan"), ("HL", "Halal"), ("KS", "Kosher"), ("GF", "Gluten-Free")]
    # username = models.ForeignKey(Username, on_delete=models.CASCADE)
    choices = models.CharField(max_length=500, choices=list_choices) 
    def __str__(self):
        return self.list_choices

class Distance(models.Model):
    # username = models.ForeignKey(Username, on_delete=models.CASCADE)
    distance_integer = models.IntegerField()
    def __str__(self):
        return self.distance_integer

class Address(models.Model):
    # username = models.ForeignKey(Username, on_delete=models.CASCADE)
    address_text = models.CharField(max_length=100)
    def __str__(self):
        return self.address_text 

class Hurry(models.Model):
    # username = models.ForeignKey(Username, on_delete=models.CASCADE)
    hurry_choice = models.BooleanField()
    def __str__(self):
        return self.hurry_choice 

class Time(models.Model):
    # username = models.ForeignKey(Username, on_delete=models.CASCADE)
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