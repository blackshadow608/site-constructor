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
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(verbose_name='image', max_length=255)),
                ('user', models.ForeignKey(default='', to=settings.AUTH_USER_MODEL)),
=======
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='')),
>>>>>>> 6484bd31294fdb56ca3f8a576d36dbc8cd850af5
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
=======
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
>>>>>>> 6484bd31294fdb56ca3f8a576d36dbc8cd850af5
            ],
        ),
        migrations.CreateModel(
            name='PageProject',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
=======
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
>>>>>>> 6484bd31294fdb56ca3f8a576d36dbc8cd850af5
                ('page_name', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
=======
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
>>>>>>> 6484bd31294fdb56ca3f8a576d36dbc8cd850af5
                ('project_name', models.CharField(max_length=100)),
                ('project_is_dark', models.BooleanField(default=False)),
                ('project_menu_is_horizontal', models.BooleanField(default=False)),
                ('project_user', models.ForeignKey(default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Raitng',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
=======
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
>>>>>>> 6484bd31294fdb56ca3f8a576d36dbc8cd850af5
                ('raiting_project', models.ForeignKey(to='article.Project')),
            ],
        ),
        migrations.AddField(
            model_name='pageproject',
            name='project',
            field=models.ForeignKey(default='', to='article.Project'),
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
