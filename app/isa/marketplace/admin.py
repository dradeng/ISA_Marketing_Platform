from django.contrib import admin

from .models import Buyer,Seller, Ad, MarketUser

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Ad)
admin.site.register(MarketUser)
