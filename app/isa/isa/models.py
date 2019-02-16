from django.db import models

class ad(models.Model):
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    duration = models.IntegerField(default=0)
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    