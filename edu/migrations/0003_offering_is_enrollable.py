# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_auto_20160802_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='is_enrollable',
            field=models.BooleanField(default=False),
        ),
    ]