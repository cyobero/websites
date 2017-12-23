# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from databaseAnalysis.models import Customer, Dealership, Dealer, Vehicle, Service

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass

class DealershipAdmin(admin.ModelAdmin):
    pass

class DealerAdmin(admin.ModelAdmin):
    pass

class VehicleAdmin(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Dealership, DealershipAdmin)
admin.site.register(Dealer, DealerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Vehicle, VehicleAdmin)