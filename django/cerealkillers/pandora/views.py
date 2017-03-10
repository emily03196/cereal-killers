from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Username, ResponsesModel
from .forms import LoginForm, ResponsesForm, SearchResponsesForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.save()
        if form.is_valid():
            # user_id = form.cleaned_data['user_id']
            username = form.cleaned_data['username']
            # return HttpResponseRedirect('%s' % username)
            # return HttpResponseRedirect('responses/')   
        return render(request, 'pandora/login.html', {'form': form, 'username_obj': username_obj, 'is_registered':True})
    else:
        form = LoginForm()
        # form.save()
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
        form.save()
        #if form.is_valid():
            #responses_obj = ResponsesModel()
            #responses_obj.diet = form.cleaned_data['diet_restrictions']
            #responses_obj.distance = form.cleaned_data['distance']
            #responses_obj.address = form.cleaned_data['address']
            #responses_obj.hurry = form.cleaned_data['hurry']
            #responses_obj.arrival_time = form.cleaned_data['time']
            #sresponses_obj.save
        return render(request, 'pandora/responses.html', {'form':form})
    else:
        form = ResponsesForm()
    return render(request, 'pandora/responses.html', {'form': form})

def searchrestaurants(request):
    if request.method == 'POST':
        form = SearchResponsesForm(request.POST)
        form.save()
        return render(request, 'pandora/searchrestaurants.html', {'form': form})
    else:
        form = SearchResponsesForm()
        # form.save()
        return render(request, 'pandora/searchrestaurants.html', {'form': form})

def recommendation(request):
    template = loader.get_template('pandora/recommendation.html')
    return HttpResponse(template.render(request))

def rejection(request):
    template = loader.get_template('pandora/rejection.html')
    return HttpResponse(template.render(request))
   
   
def index(request):
    # latest_question_list = Question.objects.order_by('pub_date')[:]
    # template = loader.get_template('pandora/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    return HttpResponseRedirect('/pandora/login')
