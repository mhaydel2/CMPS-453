from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .models import *
from decimal import *
import decimal

class GeneralView():
    template_name = 'general_calculator.html'

# use django's pre-made generic view, createview, to reduce the amount of work we need to do
class TipView(LoginRequiredMixin, generic.CreateView):

    # template that our view will render on
    template_name = 'tip_calculator'
    # form that we will use
    form_class = TipForm
    # when the form is checked for valid inputs and saved, take the user here
    success_url = 'tip_calculator'

    # if the user input is valid, do the following
    def form_valid(self, form):
        # get current user's ID and save it to the Tip object
        form.instance.userID = self.request.user
        # calculate the tip amount using subtotal and tipPercent
        subtotal = form.instance.subtotal
        tipPercent = form.instance.tipPercent
        tipAmount = subtotal * (tipPercent/100)

        # save tip amount to the form
        form.instance.tipAmount = tipAmount
        # calculate and save bill total
        billTotal = subtotal + form.instance.tipAmount
        form.instance.billTotal = billTotal

        """
        Here is where the real features come in.

        Ex: When a Tip entry is made, create a Finance entry to document this 'deduction'.
            Next, update the user's financeTotal to show the subtraction of billTotal.
        """

        # save the form
        form.save()
        return super().form_valid(form)

    # get a context dictionary to pass to the template
    def get_context_data(self, **kwargs):
        # access the createview class. Within it, use the 'get_context_data' method
        # Use the TipView as the target for the context data
        context = super(TipView, self).get_context_data(**kwargs)
        # Create a dictionary entry called 'tipCalcs' that maps to the list of Tip entries from current user
        context['tipCalcs'] = Tip.objects.filter(userID = self.request.user)
        # Return 
        return context


class InvestmentView(LoginRequiredMixin, generic.CreateView):
    
    # template that our view will render on
    template_name = 'investments'
    # form that we will use
    form_class = InvestmentForm
    # when the form is checked for valid inputs and saved, take the user here
    success_url = 'investments'

    def form_valid(self, form):
        currentUser = self.request.user
        currentUser.financeTotal -= form.instance.invTotal
        currentUser.save()

        # get current user's ID and save it to the investment object
        form.instance.userID = self.request.user
        price = form.instance.invPrice
        total = form.instance.invTotal

# calculate the price after % increase as well as the amount of profit: 
        myPercent = decimal.Decimal(.15)
        percent15 = (price + (price*myPercent))
        form.instance.percent15 = percent15
        # calculate total value of investment after % gain 
        newTotal15 = (myPercent*total)+total
        form.instance.newTotal15 = newTotal15

        # calculate the price after % increase as well as the amount of profit: 
        myPercent30 = decimal.Decimal(.30)
        percent30 = (price + (price*myPercent30))
        form.instance.percent30 = percent30
        # calculate total value of investment after % gain 
        newTotal30 = (myPercent30*total)+total
        form.instance.newTotal30 = newTotal30

        # calculate the price after % increase as well as the amount of profit: 
        myPercent50 = decimal.Decimal(.50)
        percent50 = (price + (price*myPercent50))
        form.instance.percent50 = percent50
        # calculate total value of investment after % gain 
        newTotal50 = (myPercent50*total)+total
        form.instance.newTotal50 = newTotal50

        # calculate the price after % increase as well as the amount of profit: 
        myPercent75 = decimal.Decimal(.75)
        percent75 = (price + (price*myPercent75))
        form.instance.percent75 = percent75
        # calculate total value of investment after % gain 
        newTotal75 = (myPercent75*total)+total
        form.instance.newTotal75 = newTotal75

        myPercent100 = decimal.Decimal(1.0)
        percent100 = (price + price)
        form.instance.percent100 = percent100
        # calculate total value of investment after % gain 
        newTotal100 = total+total
        form.instance.newTotal100 = newTotal100


        # save the form
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # access the createview class. Within it, use the 'get_context_data' method
        # Use the TipView as the target for the context data
        context = super(InvestmentView, self).get_context_data(**kwargs)
        # Create a dictionary entry called 'tipCalcs' that maps to the list of Tip entries from current user
        context['invCalcs'] = Investment.objects.filter(userID = self.request.user)
        # Return 
        return context


class FinanceView(LoginRequiredMixin, generic.CreateView):
    template_name = 'finance_calculator'
    form_class = FinanceForm
    success_url = 'finance_calculator'
    def form_valid(self, form):
        currentUser = self.request.user
        currentUserTotal = currentUser.financeTotal
        form.instance.userID = self.request.user
        value = form.instance.value
    
        radio = form.instance.transaction
            
        if currentUserTotal is None:
            if radio == 'DP':
                currentUserTotal = value
            else:
                currentUserTotal = 0 - value
        else:
            if radio == 'DP':
                currentUserTotal = Decimal(value + currentUserTotal)
            elif radio == 'DD':
                currentUserTotal = Decimal(currentUserTotal - value)
        form.instance.financeTotal = currentUserTotal
        currentUser.financeTotal = currentUserTotal
    
        currentUser.save()
    
        form.save()
        return super().form_valid(form)
 
        # get a context dictionary to pass to the template * pass info back to finance_calculator
    def get_context_data(self, **kwargs):
        finances = Finance.objects.filter(userID = self.request.user.id)
        context = super(FinanceView, self).get_context_data(**kwargs)
        context['finances'] = finances
        return context
