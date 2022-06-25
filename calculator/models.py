from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from users.models import *

class Tip(models.Model):
    userID = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True,)
    subtotal = models.DecimalField(decimal_places=2, max_digits=50)
    tipPercent = models.DecimalField(decimal_places=2, max_digits=50)
    tipAmount = models.DecimalField(decimal_places=2, max_digits=50, null=True, blank=True,)
    billTotal = models.DecimalField(decimal_places=2, max_digits=50, null=True, blank=True,)

    objects = models.Manager()

    def __float__(self):
        return self


class Finance(models.Model):
      
   FINANCE_CHOICES = (
       ('DP', 'Deposit'),
       ('DD', 'Deduction'),
   )
   userID = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,)
   entryName = models.TextField(max_length=150,)
   entryDate = models.DateField(auto_now=False)
   transaction = models.CharField(max_length=2, choices=FINANCE_CHOICES,)
   value = models.DecimalField(decimal_places=2, max_digits=50)
   financeTotal = models.DecimalField(decimal_places=2, max_digits=50, null=False, blank=False, default=0)
 
   objects = models.Manager()
 
   def __str__(self):
       return self.entryName


class Investment(models.Model):

    userID = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,)

    invName = models.TextField(max_length=150,)
    invTotal = models.DecimalField(decimal_places=2, max_digits=50)
    invPrice = models.DecimalField(decimal_places=2, max_digits=50)
    percent15 = models.DecimalField(decimal_places=2, max_digits=50)
    percent30 = models.DecimalField(decimal_places=2, max_digits=50)
    percent50 = models.DecimalField(decimal_places=2, max_digits=50)
    percent75 = models.DecimalField(decimal_places=2, max_digits=50)
    percent100 = models.DecimalField(decimal_places=2, max_digits=50)
    newTotal15 = models.DecimalField(decimal_places=2, max_digits=50)
    newTotal30 = models.DecimalField(decimal_places=2, max_digits=50)
    newTotal50 = models.DecimalField(decimal_places=2, max_digits=50)
    newTotal75 = models.DecimalField(decimal_places=2, max_digits=50)
    newTotal100 = models.DecimalField(decimal_places=2, max_digits=50)

     

    
    objects = models.Manager()

    def __str__(self):
        return self.invName

