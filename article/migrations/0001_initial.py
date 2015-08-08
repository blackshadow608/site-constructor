# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('page_name', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('project_name', models.CharField(max_length=100)),
                ('project_is_dark', models.BooleanField(default=False)),
                ('project_menu_is_horizontal', models.BooleanField(default=False)),
                ('project_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Raitng',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('raiting_project', models.ForeignKey(to='article.Project')),
            ],
        ),
        migrations.AddField(
            model_name='pageproject',
            name='project',
            field=models.ForeignKey(to='article.Project', default=''),
        ),
        migrations.AddField(
            model_name='like',
            name='raiting',
            field=models.ForeignKey(to='article.Raitng'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
