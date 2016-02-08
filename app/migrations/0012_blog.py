# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_person_mantra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('name_fixed', models.CharField(max_length=500)),
                ('body', models.TextField(max_length=10000)),
                ('date', models.DateTimeField()),
                ('techs', models.ManyToManyField(to='app.Tech')),
            ],
        ),
    ]
