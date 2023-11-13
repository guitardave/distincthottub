from django.db import models
from django.contrib.auth.models import User


class InternalUser(User):
    position = models.CharField(default=None, blank=True, null=True)
