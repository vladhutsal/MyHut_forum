from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist

# шо робити з формами у яких однакові поля?

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your Hut alias, cossack?'}))
    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Code word?'}))

    def clean(self):
        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')
        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    raise forms.ValidationError('Your code word is wrong!')
            except ObjectDoesNotExist:
                raise forms.ValidationError('There are no cossack like you in our Hut!')
        return super(UserLoginForm, self).clean()


class UserRegForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Your cossack alias?'}))
    password = forms.CharField(required=True,
            widget=forms.PasswordInput(attrs={'placeholder': 'What is your code word?'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        existed_usernames = User.objects.filter(username=username)

        if existed_usernames.count():
            raise forms.ValidationError('That cossack is already in our Hut!')
        return username
