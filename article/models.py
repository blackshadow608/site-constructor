from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    project_user = models.ForeignKey(User, default='')
    project_name = models.CharField(max_length=100, blank=False)
    project_is_dark = models.BooleanField(default=False)
    project_menu_is_horizontal = models.BooleanField(default=False)


class PageProject(models.Model):
    project = models.ForeignKey(Project, default='')
    page_name = models.CharField(max_length=100)
    text = models.TextField(blank=True)


class Raitng(models.Model):
    raiting_project = models.ForeignKey(Project)


class Like(models.Model):
    user = models.ForeignKey(User)
    raiting = models.ForeignKey(Raitng)


class Gallery(models.Model):
    user = models.ForeignKey(User, default='')
    image = CloudinaryField('image')

