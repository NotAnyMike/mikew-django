# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160206_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mantra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Mantra'),
        ),
    ]
