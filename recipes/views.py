from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html')


def contact(request):
    return HttpResponse('CONTACT')


def about(request):
    return HttpResponse('ABOUT')
