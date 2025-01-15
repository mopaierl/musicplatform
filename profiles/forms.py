from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User  # oder User, falls du das Standardmodell verwendest
        fields = ['username', 'email', 'password1', 'password2']
        

