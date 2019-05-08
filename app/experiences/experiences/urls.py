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
    url(r'^api/v1/ad/(?P<ad_id>\d+)/ad_detail', views.ad_detail, name='ad_detail'),
    url(r'^api/v1/login', views.login, name='login'),
    url(r'^api/v1/ad_create', views.ad_create, name='ad_create'),
    url(r'^api/v1/check_authenticator', views.check_authenticator, name='check_authenticator'),
    url(r'^api/v1/logout', views.logout, name='logout'),
    url(r'^api/v1/create_user', views.create_user, name='create_user'),
    url(r'^api/v1/search', views.search, name='search'),
    url(r'^api/v1/recommend/(?P<ad_id>\d+)$', views.get_recommendations, name='get_recommendations'),
]
