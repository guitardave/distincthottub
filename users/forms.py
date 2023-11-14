from django import forms
from .models import InternalUser


class UserForm(forms.ModelForm):

    class Meta:
        model = InternalUser
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'is_staff', 'position']