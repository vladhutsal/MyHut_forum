from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

# return render(request, 'homepage/error.html', {'error': })

def home(request):
    if request.user.is_authenticated is False:
        return redirect('login:user_login')
    else:
        return render(request, 'homepage/home.html', {
            'name': request.user,
        })
