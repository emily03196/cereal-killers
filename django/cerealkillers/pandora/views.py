from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Username, DietRestrictions, Distance, Address, Time, Hurry
from .forms import LoginForm, EnterResponsesForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # form.save()
        if form.is_valid():
            user_id = form.pk
            user_text = form.cleaned_data['user_text']
            return HttpResponseRedirect('pandora/%s' % user_text)
            # user_text = request.POST.get('user_text', '')

        # username_obj = Username(username=user_text)
        # username_obj.save()
        # user_id = user_text
        return render(request, 'pandora/login.html', {'form': form, 'username_obj': username_obj, 'is_registered':True})
    else:
        form = LoginForm()
        # form.save()
        # user_id = form.pk
        return render(request, 'pandora/login.html', {'form': form})

def processlogin(request, user_id=None):
    if user_id:
        user = Username.objects.get(id=user_id)
    else:
        user = Username(user=request.user)
    user_form = LoginForm(instance=user)
    context = {"user_id": user_id, "user_text": user_form.username}
    return render(request, "pandora/processlogin", context)

def enterresponses(request):
    if request.method == 'POST':
        form = EnterResponsesForm(request.POST)
        if form.is_valid():
            newuser = request.POST.get('newuser', '')
        diet_obj = DietRestrictions, Distance, Address, Time, Hurry
        return render(request, 'pandora/newuser.html', {'newuser_obj':newuser_obj})
    else:
        form = EnterResponsesForm()
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
    # latest_question_list = Question.objects.order_by('pub_date')[:]
    # template = loader.get_template('pandora/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    return HttpResponseRedirect('/pandora/login')
