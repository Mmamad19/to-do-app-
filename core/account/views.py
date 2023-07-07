from django.shortcuts import render
from django.views.generic import ListView ,FormView,CreateView,UpdateView,DeleteView, DetailView
from .forms import siginform
# Create your views here.
class SignUpView(CreateView):
    form_class = siginform
    success_url = '/blog/post/'
    template_name = 'blog/signup.html'