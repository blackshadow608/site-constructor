from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import FormView, TemplateView
from registration.backends.default.views import RegistrationView
from django.shortcuts import render_to_response
from django.contrib import auth
from article.forms import CreateProjectForm, DeleteProjectForm
from article.models import Project
from django.template import RequestContext


def main(request):
    output = Project.objects.values('project_name', 'project_user')
    return render_to_response('base.html', {'user': request.user, "output": output})


def logout(request):
    auth.logout(request)
    return redirect('/')


def valid_form(form,request):
    if form.is_valid():
        Project.objects.create(project_name=form.cleaned_data['project_name'],
                               project_user=request.user)

def del_project(form):
    if form.is_valid():
        project = Project.objects.filter(id=form.cleaned_data['ids'])
        project.delete()

@login_required(login_url="/")
def user_projects(request):
    form = CreateProjectForm(request.POST)
    dela = DeleteProjectForm(request.POST)
    valid_form(form,request)
    del_project(dela)
    projects = Project.objects.filter(project_user=request.user)
    return render_to_response("user_projects.html", {'user': request.user,
                                                     'projects': projects,
                                                     'form': form,
                                                     'delete_project': dela}, RequestContext(request))


class UsrCrateProj(FormView):
    form_class = CreateProjectForm
    template_name = 'user_projects.html'
    success_url = '/'


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
