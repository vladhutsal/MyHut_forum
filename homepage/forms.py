from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from homepage.models import Topic, Comment, Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Your comment goes here',
                'class': 'form-control',
                'rows': 3,
                'cols': 40
            })
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title', 'tags', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control margin-add-topic',
                'placeholder': 'Title here'
            }),
            'text': forms.Textarea(attrs={
                    'rows': 5,
                    'placeholder': 'Here`s your topic goes', 
                    'class': 'form-control margin-add-topic'
                    }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control margin-add-topic',
                'placeholder': 'Add tags'
            })
        } 
                