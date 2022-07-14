from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
]
