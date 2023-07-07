from django.shortcuts import render, redirect
from django.views.generic import ListView ,FormView,CreateView,UpdateView,DeleteView, DetailView
from .models import tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import myform 


 #shoing tasks
class postview(LoginRequiredMixin,ListView):
    queryset=tasks.objects.all()
    context_object_name='posts'
    
#creating tasks
class create_data(LoginRequiredMixin,CreateView):
    model=tasks
    success_url='/blog/post/'
    form_class=myform

#editing tasks
class edit(LoginRequiredMixin,UpdateView):
    model=tasks
    success_url='/blog/post/'
    form_class=myform
#deleting tasks
class delete(LoginRequiredMixin,DeleteView):
    model=tasks
    success_url='/blog/post/'





    