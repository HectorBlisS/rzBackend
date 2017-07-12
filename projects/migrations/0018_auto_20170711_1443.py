# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 19:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0017_auto_20170711_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='followers',
        ),
        migrations.AddField(
            model_name='follow',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='follow',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='projects.Follow', to='projects.Project'),
        ),
    ]
