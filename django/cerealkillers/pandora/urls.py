from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^searchrestaurants/$', views.searchrestaurants, name='searchrestaurants'),
    url(r'^pickrestaurants/$', views.pickrestaurants, name='pickrestaurants'),
    url(r'^responses/$', views.responses, name='responses'),
    url(r'^recommendation/$', views.recommendation, name='recommendation'),
    url(r'^rejection/$', views.rejection, name='rejection'),
    url(r'^thankyou/$', views.thankyou, name='thankyou')

]

#    url(r'^(?P<user_id>[0-9]+)/$', views.processlogin, name="processlogin"),
