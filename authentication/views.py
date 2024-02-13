from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(request, "authentication/index.html")

def signup(request):
    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signuin.html")

def signout(request):
    pass