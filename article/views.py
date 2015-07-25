from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, TemplateView
from registration.backends.default.views import RegistrationView


class RegisterFormView(RegistrationView):
    template_name = "registration.html"


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/hello"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
