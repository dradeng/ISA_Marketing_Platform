from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.TextField(max_length=500)

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)

class Ad(models.Model):
    user = models.ForeignKey(User,
        null=True, blank=True, on_delete=models.SET_NULL)
    image = models.TextField(max_length=100, default="")
    duration = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    url = models.URLField( null=True, blank=True)
    site_title = models.CharField(max_length=255, default='Google')
