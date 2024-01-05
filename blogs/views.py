from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    home=loader.get_template('home.html')
    return HttpResponse(home.render({}))

# Create your views here.
