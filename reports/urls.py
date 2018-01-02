"""reports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^database-analysis/customers/$', database_analysis_customers, name='database-analysis-customers'),
    url(r'^database-analysis/dealerships/$', database_analysis_dealerships, name='database-analysis-dealerships'),
    url(r'^database-analysis/dealers/$', database_analysis_dealers, name='database-analysis-dealers'),
    url(r'^database-analysis/vehicles/$', database_analysis_vehicles, name='database-analysis-vehicles'),
    url(r'^database-analysis/$', database_analysis, name='database-analysis'),
    url(r'^comm-analysis/emails/$', comm_analysis_emails, name='comm-analysis-emails'),
    url(r'^comm-analysis/phones/$', comm_analysis_phones, name='comm-analysis-phones'),
    url(r'^comm-analysis/letters/$', comm_analysis_letters, name='comm-analysis-letters'),
    url(r'^comm-analysis/campaign-performance/$', comm_analysis_campaigns, name='comm-analysis-campaigns'),
    url(r'^comm-analysis/$', comm_analysis, name='comm-analysis'),
    url(r'^service-analysis/customer-service-history/$', service_analysis_history, name='service-analysis-history'),
    url(r'^service-analysis/repair-orders/$', service_analysis_ro, name='service-analysis-ro'),
    url(r'^service-analysis/order-history/$', service_analysis_orders, name='service-analysis-orders'),
    url(r'^service-analysis/$', service_analysis, name='service-analysis'),
    url(r'^vehicle-analysis/vehicle-sales/$', vehicle_analysis_sales, name='vehicle-analysis-sales'),
    url(r'^vehicle-analysis/$', vehicle_analysis, name='vehicle-analysis'),
    url(r'^executive-summary/vehicle-sales/$', executive_summary_vehicles, name='executive-summary-vehicle-sales'),
    url(r'^executive-summary/$', executive_summary, name='executive-summary'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)