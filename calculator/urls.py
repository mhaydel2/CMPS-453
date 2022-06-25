from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from calculator.views import *

urlpatterns = [
     path('tip_calculator',
         TipView.as_view(template_name="calculator/tip_calculator.html"),
         name='tip_calculator'),
    path('finance_calculator',
         FinanceView.as_view(template_name="calculator/finance_calculator.html"),
         name='finance_calculator'),
    path('investments',
         InvestmentView.as_view(template_name="calculator/investments.html"),
         name='investments'),
]
