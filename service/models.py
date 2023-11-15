from django.db import models
from django.shortcuts import reverse


class ServiceTicket(models.Model):
    customer = models.ForeignKey('customers.Customer', related_name='+', on_delete=models.DO_NOTHING)
    spa = models.ForeignKey('customers.CustomerSpa', related_name='+', on_delete=models.DO_NOTHING)
    technician = models.ForeignKey('users.InternalUser', related_name='+', on_delete=models.DO_NOTHING)
    service_date = models.DateField(default=None, blank=True)
    primary_issue = models.TextField(default=None)
    date_entered = models.DateTimeField(auto_now_add=True)
    num_visits = models.IntegerField(default=1)
    is_complete = models.BooleanField(default=False)
    date_completed = models.DateField(default=None, blank=True, null=True)
    under_warranty = models.BooleanField(default=False)
    upfront_charges = models.FloatField(default=0.00)

    def __str__(self):
        return f'{self.customer}/{self.spa}/{self.technician}'

    def get_absolute_url(self):
        return reverse('customers:customer_detail', kwargs={'id': self.customer_id})


class PartsList(models.Model):
    part_name = models.CharField(max_length=200, default=None)
    part_number = models.CharField(max_length=100, default=None)
    part_description = models.TextField(default=None)
    part_cost = models.FloatField(default=0.00)
    part_price = models.FloatField(default=0.00)
    is_discontinued = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.part_name}/{self.part_number}'

    def get_absolute_url(self):
        return reverse('service:part_list')


class Invoice(models.Model):
    service_ticket = models.ForeignKey(ServiceTicket, related_name='+', on_delete=models.DO_NOTHING)
    subtotal = models.FloatField(default=0.00)
    tax = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)
    is_paid = models.BooleanField(default=False)
    date_paid = models.DateField(default=None, blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service_ticket.customer} - {self.service_ticket}'

    def get_absolute_url(self):
        return reverse('service:invoice_list')


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='+', on_delete=models.CASCADE)
    part = models.ForeignKey(PartsList, related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    adjusted_cost = models.FloatField(default=0.0)


class Schedule(models.Model):
    service_ticket = models.ForeignKey(ServiceTicket, related_name='+', on_delete=models.CASCADE)
    date_entered = models.DateTimeField(auto_now_add=True)
    date_scheduled = models.DateTimeField(default=None, blank=True, null=True)
