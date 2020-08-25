from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist

# шо робити з формами у яких однакові поля?

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Курінне ймення, козаче?'}))
    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Твоє кодове слово?'}))

    def clean(self):
        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')
        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    raise forms.ValidationError('Кодове слово не вірне!')
            except ObjectDoesNotExist:
                raise forms.ValidationError('Нема такого козака!')
        return super(UserLoginForm, self).clean()


class UserRegForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Як тебе звуть?'}))
    password = forms.CharField(required=True,
            widget=forms.PasswordInput(attrs={'placeholder': 'Придумай кодове слово'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def clean(self):
        username = self.cleaned_data.get('username').lower()
        username_queryset = User.objects.filter(username=username)

        if username_queryset.count():
            raise forms.ValidationError('Такий козак вже є в Курені!')
        return username
