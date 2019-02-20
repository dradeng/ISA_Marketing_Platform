from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/users', views.usersGet, name='users_get'),
    path('', views.home, name='home'),
    path('api/v1/ad/', views.adGet, name='ad_get'),
    path('api/v1/ad/update/$', views.adUpdate, name='ad_upate'),
    path('api/v1/ad/delete/$', views.adDelete, name='ad_delete'),
    path('api/v1/ad/create/$', views.adCreate, name='ad_create'),
    path('api/v1/buyer/', views.buyerGet, name='buyer_get'),
    path('api/v1/buyer/update/$', views.buyerUpdate, name='buyer_update'),
    path('api/v1/buyer/delete/$', views.buyerDelete, name='buyer_delete'),
    path('api/v1/buyer/create/$', views.buyerCreate, name='buyer_create'),
    path('api/v1/seller/', views.sellerGet, name='seller_get'),
    path('api/v1/seller/update/$', views.sellerUpdate, name='seller_update'),
    path('api/v1/seller/delete/$', views.sellerDelete, name='seller_delete'),
    path('api/v1/seller/create/', views.sellerCreate, name='seller_create'),

    #trevors code
    path('adCreate/', views.adCreate, name='ad_create'),
    path('<int:ad_id>/detail', views.ad_detail, name='ad_detail'),
]
