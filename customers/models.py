import datetime

from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(default=None, max_length=200)
    contact_first = models.CharField(default=None, max_length=100)
    contact_last = models.CharField(default=None, max_length=100, blank=True, null=True)
    contact_phone = models.CharField(default=None, max_length=12)
    contact_email = models.CharField(default=None, blank=True, null=True, max_length=100)
    address1 = models.CharField(default=None, max_length=200)
    address2 = models.CharField(default=None, max_length=200, blank=True, null=True)
    intersection_note = models.CharField(default=None, blank=True, max_length=200, null=True)
    customer_since = models.IntegerField(default=datetime.datetime.now().year)
    customer_notes = models.TextField(blank=True, null=True)


class CustomerSpa(models.Model):
    customer = models.ForeignKey(Customer, related_name='+', on_delete=models.CASCADE)
    spa_make = models.CharField(default=None, max_length=200)
    spa_model = models.CharField(default=None, max_length=100)
    spa_subpanel = models.CharField(default=None, max_length=100, blank=True, null=True)
    water_system = models.CharField(default=None, max_length=100, blank=True, null=True)
    serial_number = models.CharField(default=None, max_length=100, blank=True, null=True)
    installed_date = models.DateField(default=None, blank=True, null=True)


