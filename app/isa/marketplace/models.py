from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.TextField(max_length=500)

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)

class Ad(models.Model):
    image = models.TextField(max_length=100)
    duration = models.IntegerField(default=0)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, default=None)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    url = models.URLField( null=True, blank=True)
    site_title = models.CharField(max_length=255, default='google.com')

    @classmethod
    def create(image, duration, User, cost):
        AdCreated = cls(image=image, User = User, duration=duration, cost=cost, url=url, site_title=site_title)
        return AdCreated
