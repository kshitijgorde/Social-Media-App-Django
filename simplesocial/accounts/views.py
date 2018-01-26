from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import CreateView
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') # On successful signup reverse to login page
    template_name = 'accounts/signup.html'
