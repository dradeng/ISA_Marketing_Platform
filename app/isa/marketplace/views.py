from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Ad
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import AdForm


# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
def adCreate(request):
    if request.method == "POST":
        image=request.POST['image'],
        duration=request.POST['duration'],
        user=request.user,
        cost=request.POST['cost'],
        url = request.POST['url'],
        site_title = request.POST['site_title']
        form_data={'image' : 'iamge', 'duration' : 'duration', 'cost' : 'cost', 'url' : 'url', 'site_title' : 'site_title'}
        form = AdForm(data = form_data)
        if(form.is_valid):
            #User = user.objects.get(user_id=request.user.id)
            createdAd = Ad(image=image, duration=duration, user=user, cost=cost, url=url, site_title=site_title)
            createdAd.save()
            return redirect('home')
    return redirect('home')


# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
def adDelete(request):
    Ad.objects.filter(id=request.DELETE['id']).delete()
    return


# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
def adUpdate(request):
    updatedAd = Ad.objects(id = request.POST['id'])
    updatedAd.image = request.POST['image'] if request.POST['image'] else updatedAd.image
    updatedAd.duration = request.POST['duration'] if request.POST['duration'] else updatedAd.duration
    updatedAd.cost = request.POST['cost'] if request.POST['cost'] else updatedAd.cost
    updatedAd.url = request.POST['url'] if request.POST['url'] else updatedAd.url
    updatedAd.site_title = request.POST['site_title'] if request.POST['site_title'] else updatedAd.site_title
    updatedAd.save()
    return


# @route   GET views.adGet
# @desc    render individual ad
# @access  Public
def adGet(request):
    return Ad.objects.get(id=request.POST['id'])




# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
def buyerCreate(request):
    if request.method == "POST":
        image=request.POST['image'],
        duration=request.POST['duration'],
        user=request.user,
        cost=request.POST['cost'],
        url = request.POST['url'],
        site_title = request.POST['site_title']
        form_data={'image' : 'iamge', 'duration' : 'duration', 'cost' : 'cost', 'url' : 'url', 'site_title' : 'site_title'}
        form = AdForm(data = form_data)
        if(form.is_valid):
            #User = user.objects.get(user_id=request.user.id)
            createdAd = Ad(image=image, duration=duration, user=user, cost=cost, url=url, site_title=site_title)
            createdAd.save()
            return redirect('home')
    return redirect('home')


# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
def buyerDelete(request):
    Ad.objects.filter(id=request.DELETE['id']).delete()
    return


# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
def buyerUpdate(request):
    updatedAd = Ad.objects(id = request.POST['id'])
    updatedAd.image = request.POST['image'] if request.POST['image'] else updatedAd.image
    updatedAd.duration = request.POST['duration'] if request.POST['duration'] else updatedAd.duration
    updatedAd.cost = request.POST['cost'] if request.POST['cost'] else updatedAd.cost
    updatedAd.url = request.POST['url'] if request.POST['url'] else updatedAd.url
    updatedAd.site_title = request.POST['site_title'] if request.POST['site_title'] else updatedAd.site_title
    updatedAd.save()
    return


# @route   GET views.adGet
# @desc    render individual ad
# @access  Public
def buyerGet(request):
    return Ad.objects.get(id=request.POST['id'])





# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
def sellerCreate(request):
    if request.method == "POST":
        image=request.POST['image'],
        duration=request.POST['duration'],
        user=request.user,
        cost=request.POST['cost'],
        url = request.POST['url'],
        site_title = request.POST['site_title']
        form_data={'image' : 'iamge', 'duration' : 'duration', 'cost' : 'cost', 'url' : 'url', 'site_title' : 'site_title'}
        form = AdForm(data = form_data)
        if(form.is_valid):
            #User = user.objects.get(user_id=request.user.id)
            createdAd = Ad(image=image, duration=duration, user=user, cost=cost, url=url, site_title=site_title)
            createdAd.save()
            return redirect('home')
    return redirect('home')


# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
def sellerDelete(request):
    Ad.objects.filter(id=request.DELETE['id']).delete()
    return


# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
def sellerUpdate(request):
    updatedAd = Ad.objects(id = request.POST['id'])
    updatedAd.image = request.POST['image'] if request.POST['image'] else updatedAd.image
    updatedAd.duration = request.POST['duration'] if request.POST['duration'] else updatedAd.duration
    updatedAd.cost = request.POST['cost'] if request.POST['cost'] else updatedAd.cost
    updatedAd.url = request.POST['url'] if request.POST['url'] else updatedAd.url
    updatedAd.site_title = request.POST['site_title'] if request.POST['site_title'] else updatedAd.site_title
    updatedAd.save()
    return


# @route   GET views.adGet
# @desc    render individual ad
# @access  Public
def sellerGet(request):
    return Ad.objects.get(id=request.POST['id'])













# @route   Get views.home
# @desc    Render home page
# @access  Private
def home(request):
    ads = Ad.objects.all()
    return render(request, 'home.html',
        {'ads': ads })

# @route   GET views.userCreate
# @desc    return ad info
# @access  Public
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    return render(request, 'ad_detail.html',
                  {'ad': ad})
