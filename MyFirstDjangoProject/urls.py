from django.contrib import admin
from django.urls import path
from firstapp import views as f_views
from cars import views as k_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', f_views.index),
    path('about/', f_views.about),
    path('contact/', f_views.contact),
    path('car/info', k_views.index),
    path('car/price', k_views.price),
    path('buy/car', k_views.buy),
]


