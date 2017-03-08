from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^newuser/$', views.newuser, name='newuser'),
    url(r'^returninguser/$', views.returninguser, name='returninguser'),
    url(r'^modifyresponses/$', views.modifyresponses, name='modifyresponses'),
    url(r'^recommendation/$', views.recommendation, name='recommendation'),
    url(r'^rejection/$', views.rejection, name='rejection')
]