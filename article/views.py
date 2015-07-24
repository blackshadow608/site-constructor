from django.shortcuts import render

# Create your views here.
from registration.backends.default.views import RegistrationView


class RegisterFormView(RegistrationView):
    template_name = "registration.html"
