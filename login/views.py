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
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid() == True:
                form.clean_username()
                form.save()
                return redirect('login:user_login')

    return render(request, 'login/signup.html')


def user_logout(request):
    logout(request)
    return redirect('login:user_login')

def test(request):
    form = UserCreationForm
    context = {
        'form': form,
    }
    return render(request, 'login/test.html', context)