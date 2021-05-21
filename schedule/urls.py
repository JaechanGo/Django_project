from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    url(r'^schedules/$', views.schedule_list, name='schedule_list'),
    #url(r'^schedules/create/$', views.book_create, name='book_create'),
    url(r'^schedules/create/$', views.book_create, name='book_create'),
    url(r'^schedules/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^schedules/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]
