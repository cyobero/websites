from django.shortcuts import render
from databaseAnalysis.models import Customer, Dealership, Dealer, Vehicle
from commAnalysis.models import EmailCommunication, PhoneCommunication, LettersCommunication
from serviceAnalysis.models import CustomerServiceHistory, RepairOrders


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