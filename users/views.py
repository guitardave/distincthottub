from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView

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


class UserDetail(IsStaffMixin, DetailView):
    model = InternalUser
    template_name = 'users/user_detail.html'

    def get_queryset(self):
        return InternalUser.objects.get(id=self.kwargs['id'])


class UserUpdate(IsStaffMixin, UpdateView):
    model = InternalUser
    template_name = 'users/user_update.html'
    form_class = UserForm

    def form_valid(self, form):
        user = form.save(commit=True)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return redirect('users:user-profile', self.kwargs.get('pk'))
