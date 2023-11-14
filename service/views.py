from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

import users.models
from customers.models import *
from .models import *
from .forms import ServiceForm, ServiceFormBlank


class IsStaffMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('users:user_login')


class ServiceTicketList(IsStaffMixin, ListView):
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


class ServiceTicketScratch(IsStaffMixin, CreateView):
    model = ServiceTicket
    template_name = 'service/ticket_form.html'
    context_object_name = 'out'
    form_class = ServiceFormBlank

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Create Service Ticket'
        data['out'] = self.context_object_name
        return data


@login_required(login_url='/users')
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


@login_required(login_url='/users')
def update_service_ticket(request, id, pk):
    ticket = ServiceTicket.objects.get(pk=pk)
    if request.method == 'POST':
        form = ServiceFormBlank(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service Request updated successfully')
            return redirect('service:ticket_list')

    context = {'title': 'Update Service Ticket', 'form': ServiceFormBlank(instance=ticket)}
    return render(request, 'service/ticket_form.html', context)


class ServiceTicketDetail(IsStaffMixin, DetailView):
    model = ServiceTicket
    template_name = 'service/ticket_detail.html'

    def get_queryset(self):
        return ServiceTicket.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Service Detail'
        return data


@login_required(login_url='/users')
def schedule_list(request):
    out = []
    techs = users.models.InternalUser.objects.filter(position='Technician', is_active=True)
    for t in techs:
        obj = ServiceTicket.objects.filter(is_complete=False, technician=t).order_by('-service_date')
        for o in obj:
            out.append(dict(tech=t.first_name, service_date=o.service_date, customer_id=o.customer_id, ticket_id=o.id))
    context = {'title': 'Service Schedule', 'out': out}
    return render(request, 'service/schedule_list.html', context)
