# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseAnalysis', '0002_auto_20171220_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='msrp',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
