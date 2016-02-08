# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('name_fixed', models.CharField(max_length=500)),
                ('body', models.TextField(max_length=10000)),
                ('date', models.DateTimeField()),
                ('isBlog', models.BooleanField(default=True)),
                ('techs', models.ManyToManyField(to='app.Tech')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='techs',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
