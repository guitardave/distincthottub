from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User


class InternalUser(User):
    position = models.CharField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.position})'

    def get_absolute_url(self):
        return reverse('users:user_list')
