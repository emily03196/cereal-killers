from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Username, ResponsesModel, SearchRestaurantsModel, PickRestaurantsModel, RecommendationModel, RejectionModel
from .forms import LoginForm, ResponsesForm, SearchRestaurantsForm, PickRestaurantsForm, RecommendationForm, RejectionForm
from django.forms.models import model_to_dict
from .COPY_Audrey_User import User 
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
            # user_id = form.cleaned_data['user_id']
            username = form.cleaned_data['username']
            # return HttpResponseRedirect('%s' % username)
            return HttpResponseRedirect('/pandora/responses/')
        elif form.errors['username'] == ['Username with this Username already exists.']:
            username = form.dajta['username']
            returning_user = Username.objects.filter(username=username)[0]
            form = LoginForm(model_to_dict(returning_user), instance=returning_user)
            form.save()
            return HttpResponseRedirect('/pandora/responses/')            
    else:
        form = LoginForm()
        # user_id = form.pk
        return render(request, 'pandora/login.html', {'form': form})

#def processlogin(request, user_id=None):
#    if user_id:
#        user = Username.objects.get(id=user_id)
#    else:
#        user = Username(user=request.user)
#    user_form = LoginForm(instance=user)
#    context = {"user_id": user_id, "username": user_form.username}
#    return render(request, "pandora/processlogin", context)

def responses(request):
    if request.method == 'POST':
        form = ResponsesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pandora/searchrestaurants/')
    else:
        form = ResponsesForm()
    return render(request, 'pandora/responses.html', {'form': form})

def searchrestaurants(request):
    if request.method == 'POST':
        form = SearchRestaurantsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pandora/pickrestaurants/')
    else:
        form = SearchRestaurantsForm()
        # form.save()
        return render(request, 'pandora/searchrestaurants.html', {'form': form})

def pickrestaurants(request):
    if request.method == 'POST':
        form = PickRestaurantsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pandora/recommendation/')
    else:
        form = PickRestaurantsForm()
        # form.save()
        return render(request, 'pandora/pickrestaurants.html', {'form': form})

def recommendation(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get('accept') != True:
                return HttpResponseRedirect('/pandora/rejection/')
            else: 
                return HttpResponseRedirect('/pandora/thankyou/')
    else:
        form = RecommendationForm()
        return render(request, 'pandora/recommendation.html', {'form': form})

def rejection(request):
    if request.method == 'POST':
        form = RejectionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pandora/responses/')
    else:
        form = RejectionForm()
        # form.save()
        return render(request, 'pandora/rejection.html', {'form': form})

def thankyou(request):   
    return render(request, 'pandora/thankyou.html')
