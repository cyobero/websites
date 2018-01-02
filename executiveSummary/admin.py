# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from executiveSummary.models import VehicleSalesExecutive

# Register your models here.
class VehicleSalesExecutiveAdmin(admin.ModelAdmin):
    pass


admin.site.register(VehicleSalesExecutive, VehicleSalesExecutiveAdmin)

