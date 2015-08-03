# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150802_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_is_dark',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='project_menu_is_horizontal',
            field=models.BooleanField(default=False),
        ),
    ]
