from django.db import models

class Ad(models.Model):
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    duration = models.IntegerField(default=0)
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=20, decimal_places=2)


class Seller(models.Model):
    username = models.TextField(max_length=500)
    name = models.TextField(max_length=500)
    email = models.EmailField(max_length=254)
    password = models.IntegerField(default=0)
    company = models.TextField(max_length=500)
