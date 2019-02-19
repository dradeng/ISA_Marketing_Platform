from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Ad
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import AdForm




# @route   POST views.login
# @desc    Login user
# @access  Public
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #redirect
        return HttpResponseRedirect('/')
    #invalid login
    return HttpResponseRedirect('/')

# @route   Get views.home
# @desc    Render home page
# @access  Private
def home(request):
    ads = Ad.objects.all()
    return render(request, 'home.html',
        {'ads': ads })

# @route   POST views.userCreate
# @desc    Login user
# @access  Private
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

# @route   DELETE views.userDelete
# @desc    Delete a user
# @access  Private
def userDelete(request):
    User.objects.filter(id=request.DELETE['id']).delete()
    return


# @route   POST views.userUpdate
# @desc    update user info
# @access  Private
def userUpdate(request):
    updatedUser = request.user
    updatedUser.password = request.POST['password'] if request.POST['password'] else updatedUser.password
    updatedUser.username = request.POST['username'] if request.POST['username'] else updatedUser.username
    updatedUser.email = request.POST['email'] if request.POST['email'] else updatedUser.email
    updatedUser.company = request.POST['company'] if request.POST['company'] else updatedUser.company
    updatedUser.name = request.POST['name'] if request.POST['name'] else updatedUser.name
    updatedUser.save()
    return

# @route   GET views.userGet
# @desc    return user object
# @access  Private
def userGet(request):
    return request.user


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

# @route   GET views.userCreate
# @desc    return ad info
# @access  Public
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    return render(request, 'ad_detail.html',
                  {'ad': ad})
