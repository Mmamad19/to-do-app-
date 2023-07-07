from django import forms 
from .models import tasks
from django.contrib.auth.forms import UserCreationForm

class myform(forms.ModelForm):
    class Meta:
        model=tasks
        fields='__all__'