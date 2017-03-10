from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^(?P<user_id>[0-9]+)/$', views.processlogin, name="processlogin"),
    url(r'^enterresponses/$', views.enterresponses, name='enterresponses'),
    url(r'^recommendation/$', views.recommendation, name='recommendation'),
    url(r'^rejection/$', views.rejection, name='rejection')
]