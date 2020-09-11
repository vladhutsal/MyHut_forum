from django.contrib.auth import login, logout, authenticate

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from login.forms import UserLoginForm, UserRegForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('homepage:home')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('username')
        passw = form.cleaned_data.get('password')
        user = authenticate(username=name, password=passw)
        login(request, user)
        return redirect('homepage:home')
    return render(request, 'login/login.html', {'form': form})
        

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('homepage:home')
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('homepage:home')
    return render(request, 'login/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login:user_login')