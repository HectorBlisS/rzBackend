# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20170711_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='user_from',
        ),
    ]
