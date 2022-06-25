"""django_project URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

Examples
--------
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',
         TemplateView.as_view(template_name="home.html"),
         name="home"),
    path('team',
         TemplateView.as_view(template_name="team.html"),
         name="team"),
    path('about',
         TemplateView.as_view(template_name="about.html"),
         name="about"),
    path('user_anly',
         TemplateView.as_view(template_name="user_anly.html"),
         name="user_anly"),
    path('ui_design',
         TemplateView.as_view(template_name="ui_design.html"),
         name="ui_design"),
    path('wireframe_page',
         TemplateView.as_view(template_name="wireframe_page.html"),
         name="wireframe_page"),
    path('user_flow_page',
         TemplateView.as_view(template_name="user_flow_page.html"),
         name="user_flow_page"),
    path('A',
         TemplateView.as_view(template_name="A perweb.html"),
         name="A"),
    path('B',
         TemplateView.as_view(template_name="B perweb.html"),
         name="B"),
    path('C',
         TemplateView.as_view(template_name="C perweb.html"),
         name="C"),
    path('D',
         TemplateView.as_view(template_name="D perweb.html"),
         name="D"),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('calculator/', include('calculator.urls')),
]

urlpatterns += staticfiles_urlpatterns()
