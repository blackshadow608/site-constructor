import json
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import FormView, TemplateView
from registration.backends.default.views import RegistrationView
from django.shortcuts import render_to_response
from django.contrib import auth
from article.forms import CreateProjectForm, DeleteProjectForm
from article.models import Project,PageProject
from django.template import RequestContext

def view_site(request):
    content = '''    <div id="droppable" class="jumbotron for-padding ui-sortable" style="border: solid 1px black; height: auto; min-height: 500px ">
        <div class="btn-group ui-sortable-handle" role="group" aria-label="Large button group"></div>
        <li class="btn-primary btn btn-block form-group draggable ui-draggable ui-draggable-handle xyi" style="width: 100%; right: auto; height: 34px; bottom: auto;"></li>
        <li class="btn-primary btn btn-block form-group draggable ui-draggable ui-draggable-handle xyi" style="width: 100%; right: auto; height: 34px; bottom: auto;"></li>
        <li class="btn-primary btn btn-block form-group draggable ui-draggable ui-draggable-handle xyi" style="width: 100%; right: auto; height: 34px; bottom: auto;"></li>
        <li class="btn-primary btn btn-block form-group draggable ui-draggable ui-draggable-handle xyi" style="width: 100%; right: auto; height: 34px; bottom: auto;"></li>
    </div>

</div>'''
    return render_to_response('view_site_template.html', {"content": content})

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
    form = CreateProjectForm()

def del_project(form):
    if form.is_valid():
        project = Project.objects.filter(id=form.cleaned_data['ids'])
        project.delete()

@login_required(login_url="/")
def user_projects(request):
    if request.method == 'GET':
        idr = request.GET.get('proj_id')
        if idr:
            p = Project.objects.filter(id= idr)
            p.delete()

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

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['proj_name'] = ''
        return context


def search_form(request):
    return render_to_response('search_form.html',{'user':request.user})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        users = User.objects.filter(username__icontains=q)
        projects = Project.objects.filter(project_name__icontains=q)
        pagesProject = PageProject.objects.filter(page_name__icontains=q)
        textOfPages = PageProject.objects.filter(text__icontains=q)
        return render_to_response('search_form.html',
            {'users': users, 'projects': projects, 'pagesProject': pagesProject,
             'textOfPages': textOfPages, 'query': q, 'user': request.user})
    else:
         return render_to_response('search_form.html',{'user': request.user})