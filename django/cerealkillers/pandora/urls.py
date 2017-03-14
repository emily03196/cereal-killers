from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^login/$', views.login, name='login'),
    #url(r'^(?P<user_id>[0-9]+)/searchrestaurants/$', views.searchrestaurants, name='searchrestaurants'),
    url(r'^(?P<user_id>[0-9]+)/pickrestaurants/$', views.pickrestaurants, name='pickrestaurants'),
    url(r'^(?P<user_id>[0-9]+)/responses/$', views.responses, name='responses'),
    url(r'^(?P<user_id>[0-9]+)/recommendation/$', views.recommendation, name='recommendation'),    
    url(r'^(?P<user_id>[0-9]+)/rejection/$', views.rejection, name='rejection'),
    url(r'^(?P<user_id>[0-9]+)/thankyou/$', views.thankyou, name='thankyou')

]

