from django.db import models


class ServiceTicket(models.Model):
    customer = models.ForeignKey('customers.Customer', related_name='+', on_delete=models.DO_NOTHING)
    spa = models.ForeignKey('customers.CustomerSpa', related_name='+', on_delete=models.DO_NOTHING)
    service_date = models.DateField(default=None, blank=True)
    primary_issue = models.TextField(default=None)
    date_entered = models.DateField(auto_now_add=True)
    under_warranty = models.BooleanField(default=False)
    charges = models.FloatField(default=0.00)
