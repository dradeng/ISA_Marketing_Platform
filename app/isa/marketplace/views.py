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
        return
    elif(request.method == "GET"):
        return
    elif(request.method == "DELETE"):
        return
    elif(reqeuest.method == "PUT"):
        return
def ad(request):

    if(request.method == "POST"):
        return
    elif(request.method == "GET"):
        return
    elif(request.method == "DELETE"):
        return
    elif(reqeuest.method == "PUT"):
        return null
