from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, redirect, render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.contrib.auth.decorators import login_required

import service.models
from service.views import IsStaffMixin
from .models import *
from .forms import *


class CustomerList(IsStaffMixin, ListView):
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


class CustomerCreate(IsStaffMixin, CreateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    form_class = CustomerForm
    context_object_name = 'out'

    def get_context_data(self, **kwargs):
        data = super(CustomerCreate, self).get_context_data(**kwargs)
        data['title'] = 'Add Customer'
        data['out'] = self.context_object_name
        return data


class CustomerDetail(IsStaffMixin, DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'

    def get_queryset(self):
        return Customer.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        spas = CustomerSpa.objects.filter(customer_id=self.kwargs['pk'])
        service_list = service.models.ServiceTicket.objects.filter(customer_id=self.kwargs['pk'])
        data = super(CustomerDetail, self).get_context_data(**kwargs)
        data['title'] = 'Customer Detail'
        data['spas'] = spas
        data['service_tix'] = service_list
        data['out'] = self.get_queryset()
        return data


class CustomerUpdate(IsStaffMixin, UpdateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    form_class = CustomerForm

    def get_success_url(self):
        return reverse('customers:customer_detail', kwargs={'pk': self.kwargs['pk']})


@login_required(login_url='/users')
def create_spa(request, pk):
    obj = Customer.objects.get(pk=pk)
    kwargs = {'pk': pk}
    if request.method == 'POST':
        form = CustomerSpaForm(request.POST or None, **kwargs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Spa created successfully')
            return redirect('customers:customer_detail', pk)
    context = {'title': 'Create new Spa', 'form': CustomerSpaForm(**kwargs), 'object': obj}
    return render(request, 'customers/spa_form.html', context)


class UpdateSpa(IsStaffMixin, UpdateView):
    model = CustomerSpa
    template_name = 'customers/spa_form.html'
    form_class = CustomerSpaForm

    def get_form_kwargs(self):
        kwargs = super(UpdateSpa, self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs


class SpaDetail(IsStaffMixin, DetailView):
    model = CustomerSpa
    template_name = 'customers/spa_detail.html'

    def get_queryset(self):
        return CustomerSpa.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        tix = service.models.ServiceTicket.objects.filter(spa_id=self.kwargs['pk'])
        data = super().get_context_data(**kwargs)
        data['title'] = 'Spa Detail'
        data['tix'] = tix
        return data
