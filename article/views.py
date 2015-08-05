import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
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
from article.forms import CreateProjectForm, CreatePageForm, GalleryImageForm
from article.models import Project, PageProject, Raitng, Like, Gallery
from django.template import RequestContext

cloudinary.config(
    cloud_name="dowzzsdtc",
    api_key="588197345913843",
    api_secret='MQgCAff-steIYQ3cKyb8L3m7_mM'
)


def view_site(request, id_project):
    if request.method == 'POST':
        data = {'page': 'hui'}
        id_p = request.POST.get('id_return_page')
        if id_p:
            p = PageProject.objects.get(id=id_p)
            data['page'] = p.text
            return HttpResponse(json.dumps(data), content_type="application/json")
    if len(id_project) < 1:
        return redirect("/my_projects/")
    pages = PageProject.objects.filter(project=Project.objects.get(id=id_project))
    project = Project.objects.get(id=id_project)
    return render_to_response('view_site_template.html',
                              {'project': project, 'pages': pages, 'user': request.user}, RequestContext(request))


def rating(request):
    if request.method == 'GET':
        data = {'response': 'hui'}
        id_rating = request.GET.get('id_delete_rating')
        if id_rating:
            rating = Raitng.objects.filter(id=id_rating)
            rating.delete()
            data['response'] = 'success'
            return HttpResponse(json.dumps(data), content_type="application/json")
    if request.method == 'GET':
        data = {'response': 'hui'}
        id_project = request.GET.get('id_project_create_rating')
        if id_project:
            p = Raitng.objects.create(raiting_project=Project.objects.get(id=id_project))
            data['response'] = 'success'
            data['id_rating'] = p.id
            return HttpResponse(json.dumps(data), content_type="application/json")


def likes(request):
    data = {'response': 'hui'}
    if request.method == 'GET':
        id_rating = request.GET.get('id_rating')
        if id_rating and request.user.is_authenticated():
            like = Like.objects.filter(raiting=Raitng.objects.get(id=id_rating), user=request.user)
            if like:
                like.delete()
            else:
                Like.objects.create(raiting=Raitng.objects.get(id=id_rating), user=request.user)
            data['response'] = num_of_likes(id_rating)
        id_rating_get_likes = request.GET.get('id_rating_get_likes')
        if id_rating_get_likes:
            data['response'] = num_of_likes(id_rating_get_likes)
    return HttpResponse(json.dumps(data), content_type="application/json")


def num_of_likes(id_rating):
    likes = Like.objects.filter(raiting=Raitng.objects.get(id=id_rating))
    return len(likes)


def main(request):
    output = Project.objects.values('project_name', 'project_user', 'id')
    form = GalleryImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return render_to_response('base.html', {'images': Gallery.objects.filter(user=request.user), 'form_img': form,
                                            'user': request.user, "output": output, },
                              RequestContext(request))


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
    success_url = "/my_projects/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


@login_required(login_url='/')
def edit_view(request, ids):
    if len(ids) < 1:
        return redirect("/my_projects/")
    current_project = Project.objects.get(id=ids)
    if current_project.project_user != request.user:
        return redirect("/my_projects")

    page_form = CreatePageForm(request.POST)
    requests_editor(request, page_form, current_project)
    save_pages(request)
    if request.method == 'POST':
        data = {'page': 'error'}
        id_p = request.POST.get('id_return_page')
        if id_p:
            p = PageProject.objects.get(id=id_p)
            data['page'] = p.text
            return HttpResponse(json.dumps(data), content_type="application/json")
    pages = PageProject.objects.filter(project=current_project)
    return render_to_response('editor.html', {'user': request.user,
                                              'project': current_project,
                                              'pages': pages,
                                              'page_form': page_form,
                                              'images': Gallery.objects.filter(user=request.user)}, RequestContext(request))


def save_pages(request):
    if request.method == 'POST':
        id_page = request.POST.get('id_page')
        if id_page:
            p = PageProject.objects.get(id=id_page)
            p.text = request.POST.get('content')
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


def theme(request):
    if request.method == 'GET':
        data = {'page': 'hui'}
        id_p = request.GET.get('proj_id')
        value = request.GET.get('is_dark')
        if id_p:
            p = Project.objects.get(id=id_p)
            if value == 'True':
                p.project_is_dark = True
            else:
                p.project_is_dark = False
            p.save()
            return HttpResponse(json.dumps(data), content_type="application/json")


def change_menu(request):
    if request.method == 'GET':
        data = {'page': 'hui'}
        id_p = request.GET.get('proj_id')
        value = request.GET.get('is_horizontal')
        if id_p:
            p = Project.objects.get(id=id_p)
            if value == 'True':
                p.project_menu_is_horizontal = True
            else:
                p.project_menu_is_horizontal = False
            p.save()
            return HttpResponse(json.dumps(data), content_type="application/json")

def get_all_pages(request):
    if request.method == 'GET':
        id_p = request.GET.get('proj_id')
        if id_p:
            pages = PageProject.objects.filter(project=Project.objects.get(id=id_p))
            all_page = []
            for page in pages:
                all_page.append({'pageID': page.id, 'pageName': page.page_name})
            return HttpResponse(json.dumps({'pages': all_page}), content_type="application/json")

