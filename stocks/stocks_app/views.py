from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import requests

# Create your views here.

def home_view(request):
    context = {
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, 'index.html', context=context)

def login_view(request):
    context = {
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, 'login.html', context=context)

def register_view(request):
    context = {
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, 'register.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            if User.objects.filter(username=username).exists():
                context = {
                    'message': "Username already exists"
                }
            form.save()
            return redirect('login_view')
        else:
            context = {
                'message': form.errors
            }
            print(form.errors)
            return render(request, 'register.html', context=context)
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            context = {
                'message': "Incorrect credentials"
            }
            return render(request, 'login.html', context=context)

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
