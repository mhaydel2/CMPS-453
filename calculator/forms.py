from django import forms
from .models import *
from users.models import *

class TipForm(forms.ModelForm):

	class Meta:
		model = Tip
		fields = ('subtotal', 'tipPercent')


class InvestmentForm(forms.ModelForm):

	class Meta:
		model = Investment
		fields = ('invName', 'invTotal', 'invPrice')


class FinanceForm(forms.ModelForm):
     
   class Meta:
       model = Finance
       fields = ('entryName', 'entryDate', 'transaction', 'value')
