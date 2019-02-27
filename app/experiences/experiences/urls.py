"""experiences URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
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
from django.conf.urls import url
from django.contrib import admin
from experiences_app import views

urlpatterns = [
    url(r'^api/v1/home', views.home, name='homepage'),
    url(r'^api/v1/ad/<int:ad_id>/detail', views.ad_detail, name='ad_detail'),
    url(r'^api/v1/login', views.login, name='login'),
    url(r'^api/v1/check_authenticator', views.check_authenticator, name='check_authenticator'),
    url(r'^api/v1/logout', views.logout, name='logout'),
]
