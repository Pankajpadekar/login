from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template("index.html")
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signuin.html")

def signout(request):
    pass