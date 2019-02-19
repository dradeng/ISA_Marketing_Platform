from django.contrib import admin

from .models import Buyer,Seller, Ad

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Ad)
