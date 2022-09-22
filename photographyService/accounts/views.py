from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUp(generic.CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm