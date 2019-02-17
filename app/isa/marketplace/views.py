from django.shortcuts import render
from django.http import HttpResponse
from .models import Ad, User
from django.template import loader

def home(request):
    ads = Ad.objects.all()
    return render(request, 'home.html',
        {'ads': ads })

def user(request):

    if(request.method == "POST"):
        if(request.POST['company'] is not None and request.POST['company'] != ''):
            newUser = User.create(
                username=request.POST['username'],
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password'],
                companey=request.POST['company']
            )
        else:
            newUser = User.create(
                username=request.POST['username'],
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
        newUser.save()
        return
    elif(request.method == "GET"):
        return request.user
    elif(request.method == "DELETE"):
        User.objects.filter(id=request.DELETE['id']).delete()
        return
    elif(reqeuest.method == "PUT"):
        return
def adCreate(request):
    newAd = Ad.create(
        image=request.POST['image'],
        duration=request.POST['duration'],
        User=request.POST['User'],
        cost=request.POST['cost'],
    )
    newAd.save()
    return
def adDelete(request):
    Ad.objects.filter(id=request.DELETE['id']).delete()
    return
def adUpdate(request):
    
    return
def adGet(request):
    return Ad.objects.get(id=request.POST['id'])
