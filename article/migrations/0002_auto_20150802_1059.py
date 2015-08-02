# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Raitng',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pageproject',
            name='project',
            field=models.ForeignKey(to='article.Project', default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
        ),
        migrations.AddField(
            model_name='raitng',
            name='raiting_project',
            field=models.ForeignKey(to='article.Project'),
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
