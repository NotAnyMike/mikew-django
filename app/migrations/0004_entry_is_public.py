# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_entry_name_fixed'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]