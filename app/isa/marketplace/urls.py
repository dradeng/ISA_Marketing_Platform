


from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^api/v1/users', views.usersGet, name='users_get'),
    url(r'^api/v1/user/update/', views.userUpdate, name='user_update'),
    url(r'^api/v1/user/delete/', views.userDelete, name='user_delete'),
    url(r'^api/v1/user/create/', views.userCreate, name='user_create'),
    url(r'^api/v1/ads/recommendation', views.recommendation, name='recommend_ad'),
    url(r'^api/v1/ads/', views.adGet, name='ad_get'),
    url(r'^api/v1/ad/(?P<ad_id>\d+)/ad_detail/', views.ad_detail, name='ad_detail'),
    url(r'^api/v1/ad/update/', views.adUpdate, name='ad_upate'),
    url(r'^api/v1/ad/delete/', views.adDelete, name='ad_delete'),
    url(r'^api/v1/ad/create/', views.adCreate, name='ad_create'),
    url(r'^api/v1/buyers/', views.buyerGet, name='buyer_get'),
    url(r'^api/v1/buyer/update/', views.buyerUpdate, name='buyer_update'),
    url(r'^api/v1/buyer/delete/', views.buyerDelete, name='buyer_delete'),
    url(r'^api/v1/buyer/create/', views.buyerCreate, name='buyer_create'),
    url(r'^api/v1/sellers/', views.sellerGet, name='seller_get'),
    url(r'^api/v1/seller/update/', views.sellerUpdate, name='seller_update'),
    url(r'^api/v1/seller/delete/', views.sellerDelete, name='seller_delete'),
    url(r'^api/v1/seller/create/', views.sellerCreate, name='seller_create'),
    url(r'^api/v1/login', views.login, name='login'),
    url(r'^api/v1/check_authenticator$', views.check_authenticator, name='check_authenticator'),
    url(r'^api/v1/logout', views.logout, name='logout')
]
