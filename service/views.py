from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import render, redirect
from django.contrib import messages

from customers.models import *
from .models import *
from .forms import ServiceForm, ServiceFormScratch


class ServiceTicketList(ListView):
    model = ServiceTicket
    template_name = 'service/ticket_list.html'
    context_object_name = 'out'

    def get_queryset(self):
        return ServiceTicket.objects.filter(is_complete=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Open Service Tickets'
        data['out'] = self.get_queryset()
        return data


class ServiceTicketScratch(CreateView):
    model = ServiceTicket
    template_name = 'service/ticket_form.html'
    context_object_name = 'out'
    form_class = ServiceFormScratch

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Create Service Ticket'
        data['out'] = self.context_object_name
        return data


class ServiceTicketNew(CreateView):
    model = ServiceTicket
    template_name = 'service/ticket_form.html'
    context_object_name = 'out'
    form_class = ServiceForm

    def get_context_data(self, **kwargs):
        # cust = customers.models.Customer.objects.get(id=self.kwargs['id'])
        data = super().get_context_data(**kwargs)
        data['title'] = 'Create Service Ticket'
        # data['cust'] = cust
        data['out'] = self.context_object_name
        return data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['id'] = self.kwargs['id']
        return kwargs


def create_service_ticket(request, id):
    cust = Customer.objects.get(id=id)
    kwargs = {'id': id}
    if request.method == 'POST':
        form = ServiceForm(request.POST, **kwargs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service Request Created Successfully')
            return redirect('customers:customer_detail', id)
    context = {'title': 'Create Service Request', 'form': ServiceForm(**kwargs), 'cust': cust}
    return render(request, 'service/ticket_form.html', context)


class ServiceTicketUpdate(UpdateView):
    model = ServiceTicket
    template_name = 'service/ticket_form.html'
    context_object_name = 'out'
    form_class = ServiceForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['id'] = self.kwargs['id']
        return kwargs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        cust = Customer.objects.get(id=self.kwargs['id'])
        data['title'] = 'Update Service Request'
        data['cust'] = cust
        data['out'] = self.context_object_name
        return data
