

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
     path(
        '<int:ad_id>/detail',
        views.ad_detail,
        name='ad_detail'),
]
