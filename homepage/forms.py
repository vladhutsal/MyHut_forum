from django import forms
from homepage.models import Topic, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Your comment goes here',
                'class': 'form-control',
                'rows': 3,
                'cols': 40,
                'name': 'text'
            })
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Topic title'
            }),
            'text': forms.Textarea(attrs={
                    'rows': 5,
                    'placeholder': 'Topic text',
                    'class': 'form-control'
                    }),
        }
