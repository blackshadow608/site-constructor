from django import forms
# from django.contrib.auth.models import User
# from article.models import Project, PageProject
#
# __author__ = 'evgen'
#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']
#
#  class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['username']
#
# class PageForm(forms.ModelForm):
#     class Meta:
#         model = PageProject
#         fields = ['username']
from django.forms import ModelForm
from article.models import Project


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_user', 'project_name']


class DeleteProjectForm(forms.Form):
    ids = forms.IntegerField(label='id')
