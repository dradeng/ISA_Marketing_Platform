from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    #username = models.TextField(max_length=500, unique=True) #this is covered in AbstractUser
    name = models.TextField(max_length=500)
    #email = models.EmailField(max_length=254, unique=True) #this is covered in AbstractUser
    #password = models.IntegerField(default=0) #this is covered in AbstractUser
    company = models.TextField(max_length=500)

    @classmethod
    def create(username, name, email, password, company):
        userCreated = cls(username=username, name=name, email=email, password=password, company=company)
        return userCreated
    @classmethod
    def create(username, name, email, password):
        userCreated = cls(username=username, name=name, email=email, password=password)
        return userCreated

class Ad(models.Model):
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    duration = models.IntegerField(default=0)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    site_title = models.CharField(max_length=255, verbose_name=_('Title'))


    @classmethod
    def create(image, duration, User, cost):
        AdCreated = cls(image=image, User = User, duration=duration, cost=cost, url=url, site_title=site_title)
        return AdCreated
