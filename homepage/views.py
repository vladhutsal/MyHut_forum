from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from homepage.models import Topic, Comment, Tag

# return render(request, 'homepage/error.html', {'error': })

def home(request):
    if request.user.is_authenticated is False:
        return redirect('login:user_login')
    else:
        topic_names = Topic.objects.all()
        context = {
            'name': request.user,
            'topic_names': topic_names
            }
        return render(request, 'homepage/home.html', context)

def test(request):
    return render(request, 'homepage/test.html')
