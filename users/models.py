"""Accounts models."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from calculator.models import *

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """Custom User class."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    financeTotal = models.DecimalField(default=0, decimal_places=2, max_digits=50, null=True, blank=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """Return email as the object's string representation."""
        return self.email
