from django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
class meta:
    model = User
    fields = ['username', 'email', 'password1','password2']
    widgets = {
         'username': forms.TextInput(attrs={'class': 'form-control'})
    }