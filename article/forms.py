from django import forms

from django.forms import ModelForm
from article.models import Project, PageProject


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_user', 'project_name']


class CreatePageForm(ModelForm):
    class Meta:
        model = PageProject
        fields = ['project', 'page_name']
