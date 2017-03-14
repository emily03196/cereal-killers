from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Username, ResponsesModel, SearchRestaurantsModel, PickRestaurantsModel, RecommendationModel, RejectionModel, SearchChoicesModel
from .forms import LoginForm, ResponsesForm, SearchRestaurantsForm, PickRestaurantsForm, RecommendationForm, RejectionForm
from django.forms.models import model_to_dict
#import sys
#sys.path.append('cereal_killers/django/cerealkillers/pandora')
#from cereal_killers.django.cerealkillers.pandora import Audrey_User 
from . import COPY_Audrey_User
from . import COPY_search

# http://stackoverflow.com/questions/8993749/transform-an-unbound-form-to-a-bound-one
# To update field in database: 
# Model.field = "updated value"
# Model.save()
# To get Model object from a ModelForm: Form.instance

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = form.instance.user_id
            return HttpResponseRedirect('/pandora/%s/responses/' % user_id)
        elif form.errors['username'] == ['Username with this Username already exists.']:
            username = form.data['username']
            returning_user = Username.objects.filter(username=username)[0]
            form = LoginForm(model_to_dict(returning_user), instance=returning_user)
            form.save()
            user_id = form.instance.user_id
            return HttpResponseRedirect('/pandora/%s/responses/' % user_id)
    else:
        form = LoginForm()
        return render(request, 'pandora/login.html', {'form': form})

def responses(request, user_id):
    if request.method == 'POST':        
        form = ResponsesForm(request.POST)
        if form.is_valid():
            if ResponsesModel.objects.filter(user_id=user_id):
                response_model = ResponsesModel.objects.get(user_id=user_id)
                response_model.diet = form.cleaned_data['diet']
                response_model.distance = form.cleaned_data['distance']
                response_model.address = form.cleaned_data['address']
                response_model.hurry = form.cleaned_data['hurry']
                response_model.arrival_day = form.cleaned_data['arrival_day']
                response_model.arrival_time = form.cleaned_data['arrival_time']
                response_model.save()
            else: 
                form.save()
            return HttpResponseRedirect('/pandora/%s/searchrestaurants/' % user_id)
    else:
        if ResponsesModel.objects.filter(user_id=user_id):
            response_model = ResponsesModel.objects.get(user_id=user_id)
            form = ResponsesForm(model_to_dict(response_model))
        else:
            form = ResponsesForm()
        return render(request, 'pandora/responses.html', {'form': form, 'user_id': user_id})

def searchrestaurants(request, user_id):
    if request.method == 'POST':
        form = SearchRestaurantsForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            user = Username.objects.get(user_id=user_id)
            search_model = SearchRestaurantsModel(search_query=search_query, user_id=user_id)
            search_model.save()
            return HttpResponseRedirect('/pandora/%s/pickrestaurants/' % user_id)
    else:
        if SearchRestaurantsModel.objects.filter(user_id=user_id):
            search_model = SearchRestaurantsModel.objects.filter(user_id=user_id).last()
            form = SearchRestaurantsForm(model_to_dict(search_model))
        else:
            form = SearchRestaurantsForm()
        return render(request, 'pandora/searchrestaurants.html', {'form': form, 'user_id': user_id})

def pickrestaurants(request, user_id):
    if request.method == 'POST':
        form = PickRestaurantsForm(request.POST)
        if form.is_valid():
            pick_model = PickRestaurantsModel.objects.filter(user_id=user_id).last()
            pick_model.pick_result = form.cleaned_data['pick_result']
            pick_model.save()
            form.save()
            if form.cleaned_data['search_again']==True:
                return HttpResponseRedirect('/pandora/%s/searchrestaurants/' % user_id)
            else: 
                return HttpResponseRedirect('/pandora/%s/recommendation/' % user_id)
    else:
        # http://stackoverflow.com/questions/5329586/django-modelchoicefield-filtering-query-set-and-setting-default-value-as-an-obj
        search_query_model = SearchRestaurantsModel.objects.filter(user_id=user_id).last()
        search_query = search_query_model.search_query
        list_search_results = COPY_search.search(search_query)
        if len(SearchChoicesModel.objects.filter(search_query_model=search_query_model)) <= 10:
            for item in list_search_results:
                choice = SearchChoicesModel(choice=item, search_query_model=search_query_model, user_id=user_id)
                choice.save()
        form = PickRestaurantsForm()
        form.fields['pick_result'].queryset = SearchChoicesModel.objects.filter(search_query_model=search_query_model)
        return render(request, 'pandora/pickrestaurants.html', {'form': form, 'user_id': user_id})

def recommendation(request, user_id):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get('accept') != True:
                return HttpResponseRedirect('/pandora/%s/rejection/' % user_id)
            else: 
                return HttpResponseRedirect('/pandora/%s/thankyou/'% user_id)
    else:
        user_model = Username.objects.get(user_id=user_id)
        response_model = ResponsesModel.objects.get(user_id=user_id)
        past_restaurant_models = PickRestaurantsModel.objects.filter(user_id=user_id)

        username = user_model.username
        address = response_model.address
        time = response_model.arrival_time
        time = time.strftime('%H:%M')
        time = time.replace(':', '')
        time = response_model.arrival_day + " " + time
        dietary_restriction = response_model.diet
        max_distance = response_model.distance
        been_to_dic = {}
        keywords = {'environment': None, 'service': None, 'waiting': response_model.hurry}

        for past_restaurant in past_restaurant_forms:
            been_to_dic[past_restaurant.pick_result] = past_restaurant.rating

        Pandora_User = Audrey_User(username=username, address=address, time=time, dietary_restriction=dietary_restriction, max_distance=max_distance, been_to_dic=been_to_dic, keywords=keywords)
        
        recommendation, rec_list = Pandora_User.generate_recommendation
        form = RecommendationForm()
        return render(request, 'pandora/recommendation.html', {'form': form, 'user_id': user_id, 'recommendation': recommendation})

def rejection(request, user_id):
    if request.method == 'POST':
        form = RejectionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pandora/%s/responses/' % user_id)
    else:
        form = RejectionForm()
        return render(request, 'pandora/rejection.html', {'form': form, 'user_id': user_id})

def thankyou(request, user_id):   
    return render(request, 'pandora/thankyou.html')
