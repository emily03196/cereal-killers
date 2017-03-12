from django import forms
from django.forms import ModelForm
from .models import Username, ResponsesModel, SearchRestaurantsModel, PickRestaurantsModel, RecommendationModel, RejectionModel


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
        fields = ['diet', 'distance', 'address', 'hurry', 'arrival_day', 'arrival_time']

class SearchRestaurantsForm(ModelForm):
    class Meta:
        model = SearchRestaurantsModel
        fields = ['search_query1', 'search_query2', 'search_query3', 'search_query4', 'search_query5']

class PickRestaurantsForm(ModelForm):
    class Meta:
        model = PickRestaurantsModel
        fields = ['pick_results1', 'pick_results2', 'pick_results3', 'pick_results4', 'pick_results5', 'rating1', 'rating2', 'rating3', 'rating4', 'rating5']
        
class RecommendationForm(ModelForm):
    class Meta:
        model = RecommendationModel
        fields = ['accept']

class RejectionForm(ModelForm):
    class Meta:
        model = RejectionModel
        fields = ["cuisine", "price_high", "price_low"]

