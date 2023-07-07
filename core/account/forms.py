from django import forms 
from .models import User
from django.contrib.auth.forms import UserCreationForm


class siginform(UserCreationForm):
    email=forms.EmailField(max_length=255)
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    class Meta:
        model=User
        fields = [
            'email', 
            'password1', 
            'password2', 
            ]