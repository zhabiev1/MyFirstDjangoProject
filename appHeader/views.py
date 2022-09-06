from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def container(request):
    return HttpResponse("container page")


def box(request):
    return HttpResponse("box")


def info(request):
    return HttpResponseRedirect("/container")


def description(request):
    return HttpResponsePermanentRedirect("/box")


def split(request):
    return HttpResponsePermanentRedirect("/box")


