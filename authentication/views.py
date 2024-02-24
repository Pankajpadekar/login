from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.


def home(request):
    template = loader.get_template("index.html")
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name  = fname
        myuser.last_name =  lname

        myuser.save()

        messages.success(request, "Your account have been successfully created.")

        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    return render(request, "signin.html")


def signout(request):
    pass
