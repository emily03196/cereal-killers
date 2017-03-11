from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Username, ResponsesModel, SearchRestaurantsModel, PickRestaurantsModel, RecommendationModel, RejectionModel, RestartModel
from .forms import LoginForm, ResponsesForm, SearchRestaurantsForm, PickRestaurantsForm, RecommendationForm, RejectionForm, ThankYouForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # user_id = form.cleaned_data['user_id']
            username = form.cleaned_data['username']
            # return HttpResponseRedirect('%s' % username)
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
            if form['accept'] == True:
                return HttpResponseRedirect('/pandora/thankyou/')
            else: 
                return HttpResponseRedirect('/pandora/rejection/')
    else:
        form = RecommendationForm()
        # form.save()
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
    if request.method == 'POST':
        form = ThankYouForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/pandora/login/')
        else:
            form = ThankYouForm()
            return render(request, 'pandora/thankyou.html', {'form': form})
