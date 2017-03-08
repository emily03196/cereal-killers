from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Username, DietRestrictions, Distance, Address, Time, Hurry
from .forms import LoginForm, NewUserForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
        username_obj = Username(username=username)
        username_obj.save()
        return render(request, 'pandora/login.html', {'username_obj':username_obj, 'is_registered':True})
    else:
        form = LoginForm()
    # template = loader.get_template('pandora/login.html')
    return render(request, 'pandora/login.html', {'form': form})

def newuser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            newuser = request.POST.get('newuser', '')
        diet_obj = DietRestrictions, Distance, Address, Time, Hurry
        return render(request, 'pandora/newuser.html', {'newuser_obj':newuser_obj})
    else:
        form = NewUserForm()
    # template = loader.get_template('pandora/newuser.html')
    return render(request, 'pandora/newuser.html', {'form': form})

def returninguser (request):
    template = loader.get_template('pandora/returninguser.html')
    return HttpResponse(template.render(request))

def modifyresponses(request):
    template = loader.get_template('pandora/modifyresponses.html')
    return HttpResponse(template.render(request))

def recommendation(request):
    template = loader.get_template('pandora/recommendation.html')
    return HttpResponse(template.render(request))

def rejection(request):
    template = loader.get_template('pandora/rejection.html')
    return HttpResponse(template.render(request))
   
   
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:]
    template = loader.get_template('pandora/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
