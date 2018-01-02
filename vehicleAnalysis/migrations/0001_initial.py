# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('databaseAnalysis', '0003_auto_20171220_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('region', models.CharField(choices=[('North', 'North'), ('Central', 'Central'), ('East', 'East'), ('West', 'West'), ('South', 'South')], max_length=7)),
                ('vehicle_type', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=4)),
                ('units_sold', models.IntegerField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseAnalysis.Vehicle')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Vehicle Sale',
                'verbose_name_plural': 'Vehicle Sales',
            },
        ),
    ]
