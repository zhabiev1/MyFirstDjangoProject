from django.contrib import admin
from django.urls import path
from firstapp import views
from appHeader import views as header_views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('details/', views.details),
    path('container/', header_views.container),
    path('box/', header_views.box),
    path('info/', header_views.info),
    path('description/', header_views.description),
    path('split/', header_views.split),


]







