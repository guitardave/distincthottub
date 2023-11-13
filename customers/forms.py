from django import forms
from .models import Customer, CustomerSpa


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerSpaForm(forms.ModelForm):

    class Meta:
        model = CustomerSpa
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        cust = kwargs.pop('id')
        super(CustomerSpaForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(id=cust)
        