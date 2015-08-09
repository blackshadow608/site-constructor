# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(verbose_name='image', max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PageProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('page_name', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('project_is_dark', models.BooleanField(default=False)),
                ('project_menu_is_horizontal', models.BooleanField(default=False)),
                ('project_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Raitng',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
