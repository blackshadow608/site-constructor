import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Article(models.Model):
    class Meta():
        db_table = "article"

    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

class Comments(models.Model):
    class Meta():
        db_table = "comments"

    comment_text = models.TextField()
    comment_article = models.ForeignKey(Article)

class Project(models.Model):

    project_user = models.ForeignKey(User)
    project_name = models.CharField(max_length=100)


class PageProject(models.Model):

    project = models.ForeignKey(Project)
    page_name = models.CharField(max_length = 100)
    text = models.TextField()