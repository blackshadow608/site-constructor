from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import FormView, TemplateView
from registration.backends.default.views import RegistrationView
from django.shortcuts import render_to_response
from django.contrib import auth
from article.forms import My_Model_Form
from article.models import Project
from django.template import RequestContext


def main(request):
    output = Project.objects.values('project_name', 'project_user')
    return render_to_response('base.html', {'user': request.user, "output": output})


def logout(request):
    auth.logout(request)
    return redirect('/')


def valid_form(request):
    form = My_Model_Form()
    if form.is_valid():
        username = form.cleaned_data['project_user']
        proj_name = form.cleaned_data['project_name']
        Project.objects.create(prject_name=form.cleaned_data['project_user'],
                               project_user=form.cleaned_data['project_name'])


@login_required(login_url="/")
def user_projects(request):
    form = My_Model_Form(request.POST)
    form.project_user = request.user
    if form.is_valid():
        Project.objects.create(project_name=form.cleaned_data['project_name'],
                               project_user=request.user)
    form.clean()
    projects = Project.objects.filter(project_user=request.user)
    return render_to_response("user_projects.html", {'user': request.user,
                                                     'projects': projects,
                                                     'form': form, }, RequestContext(request))


class UsrCrateProj(FormView):
    form_class = My_Model_Form
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
