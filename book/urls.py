from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    url(r'^schedules/$', views.schedule_list, name='schedule_list'),
    #url(r'^schedules/create/$', views.schedule_create, name='schedule_create'),
    url(r'^schedules/create/$', views.schedule_create, name='schedule_create'),
    url(r'^schedules/(?P<pk>\d+)/update/$', views.schedule_update, name='schedule_update'),
    url(r'^schedules/(?P<pk>\d+)/delete/$', views.schedule_delete, name='schedule_delete'),
]
