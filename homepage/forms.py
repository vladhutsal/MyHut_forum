from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from homepage.models import Topic, Comment, Tag

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
