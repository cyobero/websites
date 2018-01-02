# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from vehicleAnalysis.models import VehicleSales

class VehicleSalesAdmin(admin.ModelAdmin):
    pass


admin.site.register(VehicleSales, VehicleSalesAdmin)