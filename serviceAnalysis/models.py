# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from databaseAnalysis.models import Customer, Vehicle

# Create your models here.
class CustomerServiceHistory(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    miles = models.IntegerField(blank=True, null=True)
    service_date = models.DateField()
    last_service_miles = models.IntegerField(blank=True, null=True)
    last_service_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s for %s's %s" % (self.service, self.owner, self.vehicle.owner)

    class Meta:
        verbose_name = 'Customer Service History'
        verbose_name_plural = 'Customer Service Histories'
        ordering = ['-service_date', 'owner', ]


class RepairOrders(models.Model):
    date = models.DateField()
    mailed = models.FloatField()
    received = models.FloatField()
    responses = models.FloatField()
    received_no_response = models.FloatField()
    avg_revenue_per_ro = models.FloatField()
    total_customers = models.IntegerField()
    engaged_customers = models.IntegerField()
    disengaged_customers = models.IntegerField()
    dormant_customers = models.IntegerField()
    restricted_customers = models.IntegerField()

    def __unicode__(self):
        return '%s Repair Orders' % (str(self.date))

    class Meta:
        verbose_name = 'Repair Order'
        verbose_name_plural = 'Repair Orders'
        ordering = ['-date', ]



