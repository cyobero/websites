from django.shortcuts import render
from databaseAnalysis.models import Customer, Dealership, Dealer, Vehicle
from commAnalysis.models import EmailCommunication, PhoneCommunication, LettersCommunication, CampaignPerformance
from serviceAnalysis.models import CustomerServiceHistory, RepairOrders, OrderHistory
from vehicleAnalysis.models import VehicleSales
from executiveSummary.models import VehicleSalesExecutive


def home(request):
    return render(request, 'index.html')


def database_analysis(request):
    return render(request, 'database-analysis.html')


def database_analysis_customers(request):
    customers = Customer.objects.all()
    return render(request, 'database-analysis-customers.html', {'customers': customers})


def database_analysis_dealerships(request):
    dealerships = Dealership.objects.all()
    return render(request, 'database-analysis-dealerships.html', {'dealerships': dealerships})


def database_analysis_dealers(request):
    dealers = Dealer.objects.all()
    return render(request, 'database-analysis-dealers.html', {'dealers': dealers})


def database_analysis_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'database-analysis-vehicles.html', {'vehicles': vehicles})


def comm_analysis(request):
    return render(request, 'comm-analysis.html')


def comm_analysis_emails(request):
    emails = EmailCommunication.objects.all()
    return render(request, 'comm-analysis-emails.html', {'emails': emails})


def comm_analysis_phones(request):
    phones = PhoneCommunication.objects.all()
    return render(request, 'comm-analysis-phones.html', {'phones': phones})


def comm_analysis_letters(request):
    letters = LettersCommunication.objects.all()
    return render(request, 'comm-analysis-letters.html', {'letters': letters})


def service_analysis(request):
    return render(request, 'service-analysis.html')


def service_analysis_history(request):
    histories = CustomerServiceHistory.objects.all()
    return render(request, 'service-analysis-history.html', {'histories': histories})


def service_analysis_ro(request):
    ros = RepairOrders.objects.all()
    return render(request, 'service-analysis-ro.html', {'ros': ros})


def vehicle_analysis(request):
    return render(request, 'vehicle-analysis.html')


def vehicle_analysis_sales(request):
    sales = VehicleSales.objects.all()
    return render(request, 'vehicle-analysis-sales.html', {'sales': sales})


def comm_analysis_campaigns(request):
    campaigns = CampaignPerformance.objects.all()
    return render(request, 'comm-analysis-campaigns.html', {'campaigns': campaigns})


def executive_summary(request):
    return render(request, 'executive-summary.html')


def executive_summary_vehicles(request):
    vehicles = VehicleSalesExecutive.objects.all()
    return render(request, 'executive-summary-vehicle-sales.html', {'vehicles': vehicles})


def service_analysis_orders(request):
    orders = OrderHistory.objects.all()
    return render(request, 'service-analysis-order-history.html', {'orders': orders})
