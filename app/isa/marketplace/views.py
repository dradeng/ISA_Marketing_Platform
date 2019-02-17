from django.shortcuts import render
from django.http import HttpResponse
from .models import Ad, User
from django.template import loader

def home(request):
    context = {

    }
    template = loader.get_template('base.html')
    return HttpResponse(template.render(context, request))

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
        return
    elif(request.method == "DELETE"):
        User.objects.filter(id=request.DELETE['id']).delete()
        return
    elif(reqeuest.method == "PUT"):
        return
def ad(request):

    if(request.method == "POST"):
        return
    elif(request.method == "GET"):
        return
    elif(request.method == "DELETE"):
        Ad.objects.filter(id=request.DELETE['id']).delete()
        return
    elif(reqeuest.method == "PUT"):
        return null
