from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, ListView, CreateView

from service.views import IsStaffMixin
from .models import InternalUser
from .forms import UserForm


def login_view(request):
    context = {'title': 'Login'}
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request, username=username, password=pw)
        if user is not None:
            login(request, user)
            return redirect('customers:customer_list')
        else:
            messages.info(request, 'Login Failed')
            context['form'] = AuthenticationForm()
    else:
        context['form'] = AuthenticationForm()
    return render(request, 'users/login.html', context)


@login_required(login_url='/users')
def logout_view(request):
    logout(request)
    messages.success(request, 'logout successful')
    return HttpResponseRedirect('/')


class UserList(IsStaffMixin, ListView):
    model = InternalUser
    template_name = 'users/user_list.html'
    context_object_name = 'out'

    def get_queryset(self):
        return InternalUser.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'User List'
        data['out'] = self.get_queryset()
        return data


class UserDetail(IsStaffMixin, DetailView):
    model = InternalUser
    template_name = 'users/user_detail.html'

    def get_queryset(self):
        return InternalUser.objects.filter(id=self.kwargs['pk'])


class UserCreate(IsStaffMixin, CreateView):
    model = InternalUser
    template_name = 'users/user_form.html'
    form_class = UserForm

    def form_valid(self, form):
        user = form.save(commit=True)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return redirect('users:user_list', self.kwargs.get('pk'))


class UserUpdate(IsStaffMixin, UpdateView):
    model = InternalUser
    template_name = 'users/user_form.html'
    form_class = UserForm

    def form_valid(self, form):
        user = form.save(commit=True)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return redirect('users:user_list', self.kwargs.get('pk'))
