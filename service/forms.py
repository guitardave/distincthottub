from django import forms
from .models import ServiceTicket, Schedule, PartsList, Invoice, InvoiceDetail
from customers.models import Customer, CustomerSpa


class ServiceFormBlank(forms.ModelForm):

    class Meta:
        model = ServiceTicket
        fields = '__all__'


class ServiceForm(forms.ModelForm):

    class Meta:
        model = ServiceTicket
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        cust = kwargs.pop('id')
        super(ServiceForm, self).__init__(*args, *kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(id=cust)
        self.fields['spa'].queryset = CustomerSpa.objects.filter(customer_id=cust)


class PartForm(forms.ModelForm):

    class Meta:
        model = PartsList
        fields = '__all__'


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceDetailForm(forms.ModelForm):

    class Meta:
        model = InvoiceDetail
        fields = '__all__'
