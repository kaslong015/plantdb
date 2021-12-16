from django.http import request
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base/index.html')


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')
