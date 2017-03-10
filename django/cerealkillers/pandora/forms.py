from django import forms
from django.forms import ModelForm
from .models import Username, ResponsesModel, SearchResponsesModel


class LoginForm(ModelForm): 
    # username_label = "If this is your first time using this app, enter a username of 6-12 characters. If  you are a returning user, enter your previous username."
    # username = forms.CharField(label=username_label, max_length=12, min_length=6)
    class Meta:
        model = Username
        fields = ["username", 'user_id']


class ResponsesForm(ModelForm):
    class Meta:
        model = ResponsesModel
        fields = ['diet', 'distance', 'address', 'hurry', 'arrival_day', 'arrival_time']
    # user_instance = forms.ModelChoiceField(Username, on_delete=models.CASCADE, default=None)
    
    #diet_choices = [(None, None), ("VT", "Vegetarian"),("VG", "Vegan"), ("HL", "Halal"), ("KS", "Kosher"), ("GF", "Gluten-Free")]
    #diet_label = "Select your dietary restrictions (Optional)."
    #diet_restrictions = forms.ChoiceField(required=False, label=diet_label, choices=diet_choices) 
   
    #distance_label = "What is the farthest distance (in miles) that you would be willing to travel?"
    #distance = forms.IntegerField(required=False, label=distance_label)

    #address_label = "Enter your starting address."
    #address = forms.CharField(required=False, label=address_label, max_length=100)
    
    #hurry_label = "Are you in a hurry?"
    #hurry = forms.NullBooleanField(required=False, label=hurry_label)

    #time_label = "What time will you arrive at the restaurant?"
    #time = forms.DateTimeField(required=False, label=time_label)

class SearchResponsesForm(ModelForm):
    class Meta:
        model = SearchResponsesModel
        fields = ['search_query1', 'search_query2', 'search_query3', 'search_query4', 'search_query5']
