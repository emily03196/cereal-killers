from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Username, ResponsesModel, PickRestaurantsModel, RecommendationModel, RejectionModel
from .forms import LoginForm, ResponsesForm, PickRestaurantsForm, RecommendationForm, RejectionForm
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
                response_model.environment = form.cleaned_data['environment']
                response_model.service = form.cleaned_data['service']
                response_model.arrival_day = form.cleaned_data['arrival_day']
                response_model.arrival_time = form.cleaned_data['arrival_time']
                response_model.save()
            else: 
                diet = form.cleaned_data['diet']
                distance = form.cleaned_data['distance']
                address = form.cleaned_data['address']
                hurry = form.cleaned_data['hurry']
                environment = form.cleaned_data['environment']
                service = form.cleaned_data['service']
                arrival_day = form.cleaned_data['arrival_day']
                arrival_time = form.cleaned_data['arrival_time']
                response_model = ResponsesModel(user_id=user_id, diet=diet, distance=distance, address=address, hurry=hurry, arrival_time=arrival_time, arrival_day=arrival_day, environment=environment, service=service)
                response_model.save()
            return HttpResponseRedirect('/pandora/%s/pickrestaurants/' % user_id)
    else:
        if ResponsesModel.objects.filter(user_id=user_id):
            response_model = ResponsesModel.objects.get(user_id=user_id)
            form = ResponsesForm(model_to_dict(response_model))
        else:
            form = ResponsesForm()
        return render(request, 'pandora/responses.html', {'form': form, 'user_id': user_id})
'''
def searchrestaurants(request, user_id):
    if request.method == 'POST':
        form = SearchRestaurantsForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            user = Username.objects.get(user_id=user_id)
            search_model = SearchRestaurantsModel(search_query=search_query, user_id=user_id)
            search_model.save()
            list_search_results = reversed(COPY_search.search(search_query))
            for item in list_search_results:
                choice = SearchChoicesModel(choice=item, search_query_model=search_model, user_id=user_id)
                choice.save()
            return HttpResponseRedirect('/pandora/%s/pickrestaurants/' % user_id)
    else:
        if SearchRestaurantsModel.objects.filter(user_id=user_id):
            search_model = SearchRestaurantsModel.objects.filter(user_id=user_id).last()
            form = SearchRestaurantsForm(model_to_dict(search_model))
        else:
            form = SearchRestaurantsForm()
        return render(request, 'pandora/searchrestaurants.html', {'form': form, 'user_id': user_id})
'''
def pickrestaurants(request, user_id):
    if request.method == 'POST':
        form = PickRestaurantsForm(request.POST)
        if form.is_valid():
            pick_result = form.cleaned_data['pick_result']
            rating = form.cleaned_data['rating']
            search_again = form.cleaned_data['search_again']
            pick_model = PickRestaurantsModel(user_id=user_id, pick_result=pick_result, rating=rating, search_again=search_again)
            pick_model.save()
            if form.cleaned_data['search_again']==True:
                return HttpResponseRedirect('/pandora/%s/pickrestaurants/' % user_id)
            else: 
                return HttpResponseRedirect('/pandora/%s/recommendation/' % user_id)
        return render(request, 'pandora/pickrestaurants.html', {'form': form, 'user_id': user_id})

    else:
        # http://stackoverflow.com/questions/5329586/django-modelchoicefield-filtering-query-set-and-setting-default-value-as-an-obj
        form = PickRestaurantsForm()
        return render(request, 'pandora/pickrestaurants.html', {'form': form, 'user_id': user_id})

def recommendation(request, user_id):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            accept = form.cleaned_data['accept']
            rec_model = RecommendationModel(user_id=user_id, accept=accept)
            rec_model.save()
            if accept != True:
                return HttpResponseRedirect('/pandora/%s/rejection/' % user_id)
            else: 
                return HttpResponseRedirect('/pandora/%s/thankyou/'% user_id)
    else:
        user_model = Username.objects.get(user_id=user_id)
        response_model = ResponsesModel.objects.get(user_id=user_id)
        past_restaurant_models = list(PickRestaurantsModel.objects.filter(user_id=user_id))

        username = user_model.username
        address = response_model.address
        time = response_model.arrival_time
        time = time.strftime('%H:%M')
        time = time.replace(':', '')
        time = response_model.arrival_day + " " + time
        dietary_restriction = response_model.diet
        max_distance = response_model.distance
        been_to_dic = {}
        keywords = {'environment': response_model.environment, 'service': response_model.service, 'waiting': response_model.hurry}

        for past_restaurant in past_restaurant_models:
            been_to_dic[past_restaurant.pick_result] = int(past_restaurant.rating)

        Pandora_User = COPY_Audrey_User.User(username=username, address=address, time=time, dietary_restriction=dietary_restriction, max_distance=max_distance, been_to_dic=been_to_dic, keywords=keywords)
        recommendation, rec_list = Pandora_User.generate_recommendation()
        
        if RejectionModel.objects.filter(user_id=user_id):
            rej_model = RejectionModel.objects.filter(user_id=user_id).last()
            not_cuisine = rej_model.cuisine
            price_too_high = rej_model.price_high
            price_too_low = rej_model.price_low

            recommendation, rec_list = Pandora_User.reject(rec_list, not_cuisine, price_too_high, price_too_low)
        
        if recommendation == 'No Options':
            rec_restaurant = recommendation
        else: 
            rec_restaurant = recommendation['restaurant']
            rec_address = recommendation['address']
            rec_phone = recommendation['phone']
            rec_cuisine = recommendation['cuisine_lst']
            rec_distance = recommendation['distance']
            rec_rating = recommendation['rating_score']
        form = RecommendationForm()
        return render(request, 'pandora/recommendation.html', {'form': form, 'user_id': user_id, 'rec_restaurant': rec_restaurant, 'rec_address':rec_address, 'rec_phone': rec_phone, 'rec_cuisine':rec_cuisine, 'rec_distance':rec_distance, 'rec_rating':rec_rating})

def rejection(request, user_id):
    if request.method == 'POST':
        form = RejectionForm(request.POST)
        if form.is_valid():
            rej_cuisine = form.cleaned_data['cuisine']
            rej_price_high = form.cleaned_data['price_high']
            rej_price_low = form.cleaned_data['price_low']
            rej_model = RejectionModel(user_id=user_id, cuisine=rej_cuisine, price_high=rej_price_high, price_low=rej_price_low)
            rej_model.save()
            return HttpResponseRedirect('/pandora/%s/recommendation/' % user_id)
    else:
        form = RejectionForm()
        return render(request, 'pandora/rejection.html', {'form': form, 'user_id': user_id})

def thankyou(request, user_id):   
    return render(request, 'pandora/thankyou.html')
