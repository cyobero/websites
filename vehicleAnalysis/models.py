# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from databaseAnalysis.models import Vehicle

# Create your models here.
class VehicleSales(models.Model):
    region_cohices = (
        ('North', 'North'),
        ('Central', 'Central'),
        ('East', 'East'),
        ('West', 'West'),
        ('South', 'South'),
    )

    vehicle_type_choices = (
        ('New', 'New'),
        ('Used', 'Used'),
    )

    date = models.DateField()
    region = models.CharField(max_length=7, choices=region_cohices)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=4, choices=vehicle_type_choices)
    units_sold = models.IntegerField()

    def __unicode__(self):
        return '%s Vehicle Sales for %s' % (str(self.date), self.vehicle)

    class Meta:
        verbose_name = 'Vehicle Sale'
        verbose_name_plural = 'Vehicle Sales'
        ordering = ['-date', ]

