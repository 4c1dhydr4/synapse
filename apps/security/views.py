from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LogoutView, LoginView
from .forms import (SigninForm,)

class SigninView(LoginView):
	template_name = 'security/signin.html'
	form_class = SigninForm
