from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import FormView, TemplateView
from registration.backends.default.views import RegistrationView
from django.shortcuts import render_to_response
from django.contrib import auth
from article.models import Project

def main(request):
    output = Project.objects.values('project_name', 'project_user')
    return render_to_response('base.html', {'user':request.user, "output": output})

# class HomeView(TemplateView):
#     template_name = 'base.html'
#     def render_to_response(self, context, **response_kwargs):
#         context = {}

def logout(request):
    auth.logout(request)
    return redirect('/')

class UserProjView(TemplateView):
    template_name = 'user_projects.html'

def user_projects(request):
    projects = Project.objects.filter(project_user=request.user)
    return render_to_response("user_projects.html",{'user':request.user,'projects': projects})


class RegisterFormView(RegistrationView):
    template_name = "registration.html"


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/editor/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class EditView(TemplateView):
    template_name = "editor.html"

# class Forma():
#     user = auth.get_user(request).username
