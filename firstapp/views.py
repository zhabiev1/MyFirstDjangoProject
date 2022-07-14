from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Главная страница</h1>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

