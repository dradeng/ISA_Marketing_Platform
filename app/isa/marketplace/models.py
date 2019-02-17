from django.db import models

class User(models.Model):
    username = models.TextField(max_length=500)
    name = models.TextField(max_length=500)
    email = models.EmailField(max_length=254)
    password = models.IntegerField(default=0)
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


    @classmethod
    def create(image, duration, User, cost):
        AdCreated = cls(image=image, User = User, duration=duration, cost=cost)
        return AdCreated
