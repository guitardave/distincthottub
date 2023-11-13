from django.shortcuts import HttpResponseRedirect, redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)

from .models import *
from .forms import *


class CustomerList(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'out'

    def get_queryset(self):
        return Customer.objects.all().order_by('customer_name')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(CustomerList, self).get_context_data(**kwargs)
        data['title'] = 'Customer List'
        data['out'] = self.get_queryset()
        return data


class CustomerCreate(CreateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    form_class = CustomerForm
    context_object_name = 'out'

    def get_context_data(self, **kwargs):
        data = super(CustomerCreate, self).get_context_data(**kwargs)
        data['title'] = 'Add Customer'
        data['out'] = self.context_object_name
        return data


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'

    def get_queryset(self):
        return Customer.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        data = super(CustomerDetail, self).get_context_data(**kwargs)
        data['title'] = self.get_queryset().customer_name
        data['out'] = self.get_queryset()
        return data


class CustomerSpaCreate(CreateView):
    model = CustomerSpa
    template_name = 'customers/spa_form.html'
    form_class = CustomerSpaForm

    def get_form_kwargs(self):
        kwargs = super(CustomerSpaCreate, self).get_form_kwargs()
        kwargs['id'] = self.kwargs['id']
        return kwargs
