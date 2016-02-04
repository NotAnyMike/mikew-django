# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=100)),
                ('mantra', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('facebook_username', models.CharField(max_length=50)),
                ('twitter_username', models.CharField(max_length=50)),
                ('medium_username', models.CharField(max_length=50)),
                ('github_username', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=100)),
                ('img2x', models.CharField(max_length=100)),
                ('interests', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
