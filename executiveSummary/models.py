# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
region_choices = (
    ('North', 'North'),
    ('Central', 'Central'),
    ('South', 'South'),
    ('East', 'East'),
    ('West', 'West'),
)


class VehicleSalesExecutive(models.Model):
    fiscal_year = models.IntegerField(choices=[(r, r) for r in range(1920, datetime.datetime.today().year + 2)])
    region = models.CharField(max_length=7, choices=region_choices)
    new_sold = models.IntegerField()
    used_sold = models.IntegerField()

    def total_sold(self):
        return self.new_sold + self.used_sold

    def __unicode__(self):
        return '%s Vehicle Sales Executive Report for %s Region' % (str(self.fiscal_year), self.region)

    class Meta:
        verbose_name = 'Vehicle Sales Executive Summary'
        verbose_name_plural = 'Vehicle Sales Executive Summaries'
        ordering = ['-fiscal_year', 'region', ]


class CommunicationsExecutiveSummary(models.Model):
    fiscal_year = models.IntegerField(choices=[(r, r) for r in range(1920, datetime.datetime.today().year + 2)])
    region = models.CharField(max_length=7, choices=region_choices)
    emails = models.IntegerField()
    calls = models.IntegerField()
    letters = models.IntegerField()
    texts = models.IntegerField()
    emails_received = models.IntegerField()
    calls_received = models.IntegerField()
    letters_received = models.IntegerField()
    texts_received = models.IntegerField()
    emails_responded = models.IntegerField()
    calls_responded = models.IntegerField()
    letters_responded = models.IntegerField()
    texts_responded = models.IntegerField()

    def __unicode__(self):
        return '%s Communications Executive Summary' % str(self.fiscal_year)

    class Meta:
        verbose_name = 'Communications Executive Summary'
        verbose_name_plural = 'Communications Executive Summaries'
        ordering = ['-fiscal_year', ]
