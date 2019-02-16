from django.db import models

class ad(models.Model):
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    duration = models.IntegerField(default=0)
    seller = models.ForeignKey(seller, on_delete=models.CASCADE)


class seller(models.Model):
    username = models.TextField(max_length=500)
    name = models.TextField(max_length=500)
    email = models.EmailField(max_length=254)
    password = models.IntegerField(default=0)
