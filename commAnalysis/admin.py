# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from commAnalysis.models import EmailCommunication, PhoneCommunication, LettersCommunication, CampaignPerformance

# Register your models here.
class EmailCommAdmin(admin.ModelAdmin):
    pass

class PhoneCommAdmin(admin.ModelAdmin):
    pass

class LettersCommAdmin(admin.ModelAdmin):
    pass

class CampaignPerformanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailCommunication, EmailCommAdmin)
admin.site.register(PhoneCommunication, PhoneCommAdmin)
admin.site.register(LettersCommunication, LettersCommAdmin)
admin.site.register(CampaignPerformance, CampaignPerformanceAdmin)