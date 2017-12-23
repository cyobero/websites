# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

region_choices = (
    ('Central', 'Central'),
    ('West', 'West'),
    ('South', 'South'),
    ('East', 'East'),
    ('North', 'North'),
)


class PhoneCommunication(models.Model):
    region = models.CharField(max_length=7, choices=region_choices)
    offer = models.CharField(max_length=200, blank=True, null=True)
    calls_sent = models.FloatField(default=0.0)
    calls_received = models.FloatField(default=0.0)
    call_responses = models.IntegerField(default=0.0)
    calls_received_no_response = models.FloatField(default=0.0)
    date = models.DateField()

    def response_rate(self):
        return round(self.call_responses / self.calls_sent, 3) * 100

    def reception_rate(self):
        return round(self.calls_received / self.calls_sent, 3) * 100

    def __unicode__(self):
        return '%s Region on %s' %(self.region, self.date)

    class Meta:
        verbose_name = 'Phone Communication'
        verbose_name_plural = 'Phone Communications'
        ordering = ['region', ]


class EmailCommunication(models.Model):
    region = models.CharField(max_length=7, choices=region_choices)
    offer = models.CharField(max_length=200, blank=True, null=True)
    emails_sent = models.FloatField(default=0.0)
    emails_received = models.FloatField(default=0.0)
    email_responses = models.FloatField(default=0.0)
    email_received_no_response = models.FloatField(default=0.0)
    date = models.DateField()

    def response_rate(self):
        return round(self.email_responses / self.emails_sent, 3) * 100

    def reception_rate(self):
        return round(self.emails_received / self.emails_sent, 3) * 100

    def __unicode__(self):
        return '%s Region on %s' % (self.region, self.date)

    class Meta:
        verbose_name = 'Email Communication'
        verbose_name_plural = 'Email Communications'
        ordering = ['region', ]


class LettersCommunication(models.Model):
    region = models.CharField(max_length=7, choices=region_choices)
    offer = models.CharField(max_length=200, blank=True, null=True)
    letters_sent = models.IntegerField(default=0.0)
    letters_received = models.FloatField(default=0.0)
    letter_responses = models.IntegerField(default=0.0)
    letters_received_no_response = models.FloatField(default=0.0)
    date = models.DateField()

    def response_rate(self):
        return round(self.letter_responses / float(self.letters_sent), 3) * 100

    def reception_rate(self):
        return round(self.letters_received / float(self.letters_sent), 3) * 100

    def __unicode__(self):
        return '%s Region on %s' % (self.region, self.date)

    class Meta:
        verbose_name = 'Letter Communication'
        verbose_name_plural = 'Letter Communications'
        ordering =['region', ]


class CampaignPerformance(models.Model):
    campaign = models.CharField(max_length=100)
    calls = models.IntegerField()
    emails = models.IntegerField()
    texts = models.IntegerField()
    prints = models.IntegerField()

    def total(self):
        return self.calls + self.emails + self.texts + self.prints

    def __unicode__(self):
        return self.campaign

    class Meta:
        verbose_name = 'Campaign Performance'
        verbose_name_plural = 'Campaign Performances'
        ordering = ['campaign', ]

