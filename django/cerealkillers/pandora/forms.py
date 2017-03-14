from django import forms
from django.forms import ModelForm
from .models import Username, ResponsesModel, PickRestaurantsModel, RecommendationModel, RejectionModel


class LoginForm(ModelForm): 
    # username_label = "If this is your first time using this app, enter a username of 6-12 characters. If  you are a returning user, enter your previous username."
    # username = forms.CharField(label=username_label, max_length=12, min_length=6)
    class Meta:
        model = Username
        fields = ["username", 'user_id']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

class ResponsesForm(ModelForm):
    class Meta:
        model = ResponsesModel
        fields = ['diet', 'distance', 'address', 'hurry', 'environment', 'service', 'arrival_day', 'arrival_time']
'''
class SearchRestaurantsForm(ModelForm):

    class Meta:
        model = SearchRestaurantsModel
        fields = ['search_query']
'''
class PickRestaurantsForm(ModelForm):
    class Meta:
        model = PickRestaurantsModel
        fields = ['rating', 'search_again', 'pick_result']
        
class RecommendationForm(ModelForm):
    class Meta:
        model = RecommendationModel
        fields = ['accept']

class RejectionForm(ModelForm):
    class Meta:
        model = RejectionModel
        fields = ["cuisine", "price_high", "price_low"]

