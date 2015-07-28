import datetime
from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    project_user = models.ForeignKey(User,default='')
    project_name = models.CharField(max_length=100)

class PageProject(models.Model):
    project = models.ForeignKey(Project)
    page_name = models.CharField(max_length = 100)
    text = models.TextField()