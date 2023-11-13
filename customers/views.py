from django.shortcuts import HttpResponseRedirect, redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)

from .models import *
from .forms import *


class CustomerList(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'out'


class CustomerCreate(CreateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    form_class = CustomerForm
