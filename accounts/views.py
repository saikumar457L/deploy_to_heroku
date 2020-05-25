from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse

""" we can also use this from django.views.generic import CreateView """
from django.views import generic
# Create your views here.

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")
