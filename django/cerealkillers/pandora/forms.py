from django import forms
from django.forms import ModelForm
from .models import Username


class LoginForm(ModelForm): 
    # username_label = "If this is your first time using this app, enter a username of 6-12 characters. If  you are a returning user, enter your previous username."
    # user_text = forms.CharField(label=username_label, max_length=12, min_length=6)
    class Meta:
        model = Username
        fields = ["user_text"]

class EnterResponsesForm(forms.Form):
    diet_choices = [("VT", "Vegetarian"),("VG", "Vegan"), ("HL", "Halal"), ("KS", "Kosher"), ("GF", "Gluten-Free")]
    diet_label = "Select your dietary restrictions (Optional)."
    diet_restrictions = forms.ChoiceField(required=False, label=diet_label, choices=diet_choices) 
   
    distance_label = "What is the farthest distance (in miles) that you would be willing to travel?"
    distance = forms.IntegerField(required=False, label=distance_label)

    address_label = "Enter your starting address."
    address = forms.CharField(required=False, label=address_label, max_length=100)
    
    hurry_label = "Are you in a hurry?"
    hurry = forms.BooleanField(required=False, label=hurry_label)

    time_label = "What time will you arrive at the restaurant?"
    time = forms.DateTimeField(required=False, label=time_label)
