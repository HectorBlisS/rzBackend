# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-06 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_auto_20171106_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]
