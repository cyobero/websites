# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from serviceAnalysis.models import CustomerServiceHistory, RepairOrders, OrderHistory


# Register your models here.
class CustomerServiceHistoryAdmin(admin.ModelAdmin):
    pass


class RepairOrdersAdmin(admin.ModelAdmin):
    pass


class OrderHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomerServiceHistory, CustomerServiceHistoryAdmin)
admin.site.register(RepairOrders, RepairOrdersAdmin)
admin.site.register(OrderHistory, OrderHistoryAdmin)
