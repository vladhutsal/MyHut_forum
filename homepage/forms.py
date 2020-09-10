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


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title', 'tags', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title here'
            }),
            'text': forms.Textarea(attrs={
                    'rows': 5,
                    'placeholder': 'Here`s your topic goes', 
                    'class': 'form-control'
                    }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add tags'
            })
        } 
                