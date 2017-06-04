# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170531_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=240)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reward',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='projects.Project'),
        ),
    ]
