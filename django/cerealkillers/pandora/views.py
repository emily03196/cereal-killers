from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def login(request):
    template = loader.get_template('pandora/login.html')
    return HttpResponse(template.render(request))

def newuser(request):
    template = loader.get_template('pandora/newuser.html')
    return HttpResponse(template.render(request))

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
