from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# def index(request):
#     return HttpResponse("<h1>Главная страница</h1>")
#
# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
#
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")

# def products(request, id):
#     output = f"<h2>hello, product id = {id}</h2>"
#     return HttpResponse(output)

def index(request):
    return HttpResponse("index page")


def about(request):
    return HttpResponse("about page")


def contacts(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")

