from django.shortcuts import render
from django.http import HttpResponse

def users(request, id, name):
    output = f"<h2>hello, my name is {name}, my id is {id}</h2>"
    return HttpResponse(output)
