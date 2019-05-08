from django.db import models

class MarketUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=200)


class Authenticator(models.Model):
    user = models.ForeignKey(MarketUser, on_delete=models.CASCADE)
    authenticator = models.CharField(primary_key=True, max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)


class Seller(models.Model):
    user = models.OneToOneField(MarketUser, on_delete=models.CASCADE)
    company = models.TextField(max_length=500)

class Buyer(models.Model):
    user = models.OneToOneField(MarketUser, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)

class Ad(models.Model):
    user = models.ForeignKey(MarketUser,null=True, blank=True, on_delete=models.SET_NULL)
    image = models.TextField(max_length=100, default="")
    duration = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    url = models.URLField( null=True, blank=True)
    site_title = models.CharField(max_length=255, default='Google')

class Recommendations(models.Model):
    Page_id = models.IntegerField(primary_key=True)
    Related_pages = models.CharField(max_length=200)
