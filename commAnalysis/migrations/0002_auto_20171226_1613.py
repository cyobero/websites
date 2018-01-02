# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignperformance',
            name='calls_received',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='calls_responded',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='emails_received',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='emails_responded',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='prints_received',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='prints_responded',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='texts_received',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignperformance',
            name='texts_responded',
            field=models.FloatField(blank=True, null=True),
        ),
    ]