from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('add/', views.add_message, name='add'),
    path('addRoom/', views.add_private_room, name='addRoom'),
    path('search/', views.search, name='search'),
    path('privateRoom/', views.private_room, name='private')
    ]
