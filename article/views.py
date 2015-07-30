import json
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import FormView, TemplateView
from registration.backends.default.views import RegistrationView
from django.shortcuts import render_to_response
from django.contrib import auth
from article.forms import CreateProjectForm, CreatePageForm
from article.models import Project, PageProject
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


def valid_form(form, request):
    if form.is_valid():
        Project.objects.create(project_name=form.cleaned_data['project_name'],
                               project_user=request.user)
    form = CreateProjectForm()


@login_required(login_url="/")
def user_projects(request):
    if request.method == 'GET':
        idr = request.GET.get('proj_id')
        if idr:
            p = Project.objects.filter(id=idr)
            p.delete()

    form = CreateProjectForm(request.POST)
    valid_form(form, request)
    projects = Project.objects.filter(project_user=request.user)
    return render_to_response("user_projects.html", {'user': request.user,
                                                     'projects': projects,
                                                     'form': form}, RequestContext(request))


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


def edit_view(request, ids):
    global data
    if len(ids) < 1:
        return redirect("/my_projects/")
    current_project = Project.objects.get(id=ids)
    if current_project.project_user != request.user:
        return redirect("/my_projects")
    page_form = CreatePageForm(request.POST)
    requests_editor(request, page_form, current_project)
    save_pages(request)
    if request.method == 'GET':
        data={'page':'error'}
        id_p = request.GET.get('id_return_page')
        if id_p:
            a = False
            p = PageProject.objects.get(id=id_p)
            data['page']=p.text
            return HttpResponse(json.dumps(data), content_type="application/json")
    pages = PageProject.objects.filter(project=current_project)
    return render_to_response('editor.html', {'user': request.user,
                                              'project': current_project,
                                              'pages': pages,
                                              'page_form': page_form}, RequestContext(request))


def save_pages(request):
    if request.method == 'GET':
        id_page = request.GET.get('id_page')
        if id_page:
            p = PageProject.objects.get(id=id_page)
            p.text = request.GET.get('content')
            p.save()



def requests_editor(request, form, current_project):
    if form.is_valid():
        PageProject.objects.create(project=current_project, page_name=form.cleaned_data['page_name'])
    form = CreateProjectForm()


def search_form(request):
    return render_to_response('search_form.html', {'user': request.user})


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
        return render_to_response('search_form.html', {'user': request.user})
