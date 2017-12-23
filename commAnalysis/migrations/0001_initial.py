# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.CharField(max_length=100)),
                ('calls', models.IntegerField()),
                ('emails', models.IntegerField()),
                ('texts', models.IntegerField()),
                ('prints', models.IntegerField()),
            ],
            options={
                'ordering': ['campaign'],
                'verbose_name': 'Campaign Performance',
                'verbose_name_plural': 'Campaign Performances',
            },
        ),
        migrations.CreateModel(
            name='EmailCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Central', 'Central'), ('West', 'West'), ('South', 'South'), ('East', 'East'), ('North', 'North')], max_length=7)),
                ('offer', models.CharField(blank=True, max_length=200, null=True)),
                ('emails_sent', models.FloatField(default=0.0)),
                ('emails_received', models.FloatField(default=0.0)),
                ('email_responses', models.FloatField(default=0.0)),
                ('email_received_no_response', models.FloatField(default=0.0)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['region'],
                'verbose_name': 'Email Communication',
                'verbose_name_plural': 'Email Communications',
            },
        ),
        migrations.CreateModel(
            name='LettersCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Central', 'Central'), ('West', 'West'), ('South', 'South'), ('East', 'East'), ('North', 'North')], max_length=7)),
                ('offer', models.CharField(blank=True, max_length=200, null=True)),
                ('letters_sent', models.IntegerField(default=0.0)),
                ('letters_received', models.FloatField(default=0.0)),
                ('letter_responses', models.IntegerField(default=0.0)),
                ('letters_received_no_response', models.FloatField(default=0.0)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['region'],
                'verbose_name': 'Letter Communication',
                'verbose_name_plural': 'Letter Communications',
            },
        ),
        migrations.CreateModel(
            name='PhoneCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Central', 'Central'), ('West', 'West'), ('South', 'South'), ('East', 'East'), ('North', 'North')], max_length=7)),
                ('offer', models.CharField(blank=True, max_length=200, null=True)),
                ('calls_sent', models.FloatField(default=0.0)),
                ('calls_received', models.FloatField(default=0.0)),
                ('call_responses', models.IntegerField(default=0.0)),
                ('calls_received_no_response', models.FloatField(default=0.0)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['region'],
                'verbose_name': 'Phone Communication',
                'verbose_name_plural': 'Phone Communications',
            },
        ),
    ]