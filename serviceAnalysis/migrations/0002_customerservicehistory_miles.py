# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-23 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerservicehistory',
            name='miles',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
