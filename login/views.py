from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from login.forms import UserLoginForm, UserRegForm


def user_login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('username')
        passw = form.cleaned_data.get('password')
        user = authenticate(username=name, password=passw)
        login(request, user)
        return redirect('homepage:home')
    return render(request, 'login/login.html', {'form': form})
        

def user_signup(request):
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        form.save()
        name = form.cleaned_data.get('username')
        passw = form.cleaned_data.get('password')
        new_user = authenticate(username=name, password=passw)
        login(request, new_user)
        return redirect('homepage:home')
    
    error = form.errors
    a = error.get('username')
    print(a)
    return render(request, 'login/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login:user_login')