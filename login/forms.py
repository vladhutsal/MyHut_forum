from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserLoginForm(forms.ModelForm):
    # username = forms.CharField(max_length=150, required=True)
    # password = forms.CharField(required=True)

    class Meta:
        name_attrs = {
            'placeholder': 'Your Hut alias, cossack?',
            'id': 'username_id'
        }
        pass_attrs = {'placeholder': 'Code word?'}

        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs=name_attrs),
            'password': forms.PasswordInput(attrs=pass_attrs)
        }

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
            return super().clean()


class UserRegForm(forms.ModelForm):
    # username = forms.CharField(max_length=150, required=True)
    # password = forms.CharField(required=True)

    name_attr = {'placeholder': 'Your cossack alias?'}
    pass_attr = {'placeholder': 'What is your code word?'}

    class Meta:
        name_attr = {'placeholder': 'Your cossack alias?'}
        pass_attr = {'placeholder': 'What is your code word?'}

        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs=name_attr),
            'password': forms.PasswordInput(attrs=pass_attr)
        }

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        existed_usernames = User.objects.filter(username=username)

        if existed_usernames.count():
            raise forms.ValidationError('That cossack is already in our Hut!')
        return username
