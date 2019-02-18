from django.shortcuts import render
from django.http import HttpResponse
from .models import Ad, User
from django.template import loader

def home(request):
    ads = Ad.objects.all()
    return render(request, 'home.html',
        {'ads': ads })

def userCreate(request):
    if(request.POST['company'] is not None and request.POST['company'] != ''):
        newUser = User.create(
            username=request.POST['username'],
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            company=request.POST['company']
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
def userDelete(request):
    User.objects.filter(id=request.DELETE['id']).delete()
    return
def userUpdate(request):
    updatedUser = request.user
    updatedUser.password = request.POST['password'] if request.POST['password'] else updatedUser.password
    updatedUser.username = request.POST['username'] if request.POST['username'] else updatedUser.username
    updatedUser.email = request.POST['email'] if request.POST['email'] else updatedUser.email
    updatedUser.company = request.POST['company'] if request.POST['company'] else updatedUser.company
    updatedUser.name = request.POST['name'] if request.POST['name'] else updatedUser.name
    updatedUser.save()
    return
def userGet(request):
    return request.user

def adCreate(request):
    newAd = Ad.create(
        image=request.POST['image'],
        duration=request.POST['duration'],
        User=request.user,
        cost=request.POST['cost'],
        url = request.POST['url'],
        site_title = request.POST['site_title']
    )
    newAd.save()
    return
def adDelete(request):
    Ad.objects.filter(id=request.DELETE['id']).delete()
    return
def adUpdate(request):
    updatedAd = Ad.objects(id = request.POST['id'])
    updatedAd.image = request.POST['image'] if request.POST['image'] else updatedAd.image
    updatedAd.duration = request.POST['duration'] if request.POST['duration'] else updatedAd.duration
    updatedAd.cost = request.POST['cost'] if request.POST['cost'] else updatedAd.cost
    updatedAd.url = request.POST['url'] if request.POST['url'] else updatedAd.url
    updatedAd.site_title = request.POST['site_title'] if request.POST['site_title'] else updatedAd.site_title
    updatedAd.save()
    return
def adGet(request):
    return Ad.objects.get(id=request.POST['id'])
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    return render(request, 'ad_detail.html',
                  {'ad': ad})
