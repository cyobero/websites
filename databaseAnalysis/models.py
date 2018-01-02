# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import django_localflavor_us

from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_type_choices = (
        ('Loyal', 'Loyal'),
        ('Lapsed', 'Lapsed'),
    )


    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=70, verbose_name='Last Name')
    address_one = models.CharField(max_length=80, verbose_name='Address Line 1')
    address_two = models.CharField(max_length=30, verbose_name='Address Line 2', blank=True, null=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=2, choices=django_localflavor_us.us_states.STATE_CHOICES)
    zip = models.CharField(max_length=5)
    home_phone = django_localflavor_us.models.PhoneNumberField(blank=True, null=True)
    mobile_phone = django_localflavor_us.models.PhoneNumberField(blank=True, null=True)
    work_phone = django_localflavor_us.models.PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True)
    customer_type = models.CharField(max_length=7, choices=customer_type_choices)

    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['last_name', 'first_name', ]


class Vehicle(models.Model):
    make_choices = (
        ('Kia', 'Kia'),
        ('BMW', 'BMW'),
        ('Porsche', 'Porsche'),
        ('Lexus', 'Lexus'),
        ('Honda', 'Honda'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Dodge', 'Dodge'),
        ('Chrysler', 'Chrysler'),
        ('Nissan', 'Nissan'),
        ('Jeep', 'Jeep'),
        ('Audi', 'Audi'),
        ('Toyota', 'Toyota'),
        ('MINI', 'MINI'),
        ('GMC', 'GMC'),
        ('Acura', 'Acura'),
        ('Volkswagen', 'Volkswagen'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Lincoln', 'Lincoln'),
        ('Subaru', 'Subaru'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Infinity', 'Infinity'),
        ('Lamborghini', 'Lamborghini'),
    )

    make = models.CharField(max_length=30, choices=make_choices)
    model = models.CharField(max_length=40)
    year = models.IntegerField(choices=[(r, r) for r in range(1920, datetime.datetime.today().year + 2)])
    vin = models.CharField(max_length=20, blank=True, null=True)
    msrp = models.BigIntegerField(blank=True, null=True)
    owner = models.ForeignKey(Customer, blank=True, null=True, related_name='owner')

    def __unicode__(self):
        return '%s %s %s' % (self.year, self.make, self.model)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        ordering = ['make', 'model', 'year', ]


class Service(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=140)
    date_of_service = models.DateField()
    mileage = models.BigIntegerField()
    cost = models.FloatField()

    def __unicode__(self):
        return "%s on %s's %s on %s" % (self.service_type, self.vehicle.owner, self.vehicle.model, str(self.date_of_service))

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['date_of_service', ]


class Dealership(models.Model):
    name = models.CharField(max_length=50)
    address_one = models.CharField(max_length=80, verbose_name='Address Line 1')
    address_two = models.CharField(max_length=30, verbose_name='Address Line 2', null=True, default=' ', blank=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=2, choices=django_localflavor_us.us_states.STATE_CHOICES)
    zip = models.CharField(max_length=5)
    phone = django_localflavor_us.models.PhoneNumberField(null=True, blank=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Dealership'
        verbose_name_plural = 'Dealerships'
        ordering =['name', ]


class Dealer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    title = models.CharField(max_length=50, blank=True, null=True)
    phone = django_localflavor_us.models.PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'
        ordering = ['last_name', 'first_name', 'dealership', ]


class VehicleInventory(models.Model):
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    date = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    inventory = models.IntegerField()
    condition = models.CharField(max_length=5, choices=(
        ('New', 'New'),
        ('Used', 'Used'),
    ))

    def __unicode__(self):
        return self.vehicle

    class Meta:
        verbose_name = 'Vehicle Inventory'
        verbose_name_plural = 'Vehicle Inventories'
        ordering = ['vehicle', '-date', ]