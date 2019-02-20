from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Seller, Buyer, Ad
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import AdForm
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
def adCreate(request):
    if request.method == "POST":
<<<<<<< HEAD
        try:
            user_id = request.GET.get('user')
            image = request.GET.get('image')
            cost = request.GET.get('cost')
            duration = request.GET.get('duration')
            url =request.GET.get('url')
            site_title = reques.GET.get('site_title')
            user = User.objects.get(pk=user_id)
            createdAd = Buyer(user=user, image=image, cost=cost, duration=duration,site_title=site_title, url=url)
=======
        image=request.POST['image'],
        duration=request.POST['duration'],
        user=request.user,
        cost=request.POST['cost'],
        url = request.POST['url'],
        site_title = request.POST['site_title']
        form_data={'image' : 'image', 'duration' : 'duration', 'cost' : 'cost', 'url' : 'url', 'site_title' : 'site_title'}
        form = AdForm(data = form_data)
        if(form.is_valid):
            createdAd = Ad(image=image, duration=duration, user=user, cost=cost, url=url, site_title=site_title)
>>>>>>> a17fec7fd70811a8fd607a44532e57c821792ebe
            createdAd.save()
        except:
            return HttpResponse({'ad_create_failure': "User does not exist"}, status=404)

        return HttpResponse({'ad_create_success': "Ad created successfully"}, status=200)

    return HttpResponse({"ad_create_failure": "Ad created failed"}, status=404)



# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
def adDelete(request):
    ad_object = Ad.objects.filter(pk=request.GET['pk'])
    ad_object.delete()
    return HttpResponse({"ad_delete_success": "Ad deleted successfully"}, status=200)



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
# @desc    render all ad
# @access  Public
def adGet(request):
    data = serializers.serialize("json", Ad.objects.all())
    return HttpResponse(data)




# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
def buyerCreate(request):
    if request.method == "POST":
        try:
            user_id=request.GET.get('user')
            credit=request.GET.get('credit')
            user = User.objects.get(pk=user_id)
            createdBuyer = Buyer(user=user, credit=credit)
            createdBuyer.save()
        except:
            return HttpResponse({'buyer_create_failure': "User does not exist"}, status=404)

        return HttpResponse({'buyer_create_success': "Buyer created successfully"}, status=200)

    return HttpResponse({"buyer_create_failure": "Buyer created failed"}, status=404)



# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
def buyerDelete(request):
    buyer_object = Buyer.objects.filter(pk=request.GET['pk'])
    buyer_object.delete()
    return HttpResponse({"buyer_delete_success": "Buyer deleted successfully"}, status=200)



# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
def buyerUpdate(request):
    updatedAd = Ad.objects(id = request.POST['id'])
    return


# @route   GET views.adGet
# @desc    render individual ad
# @access  Public
def buyerGet(request):
    data = serializers.serialize("json", Buyer.objects.all())
    return HttpResponse(data)

# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
@csrf_exempt
def sellerCreate(request):
    if request.method == "POST":
        try:
            user_id=request.GET.get('user')
            company=request.GET.get('company')
            user = User.objects.get(pk=user_id)
            createdSeller = Seller(user=user, company=company)
            createdSeller.save()
        except:
            return HttpResponse({'seller_create_failure': "User does not exist"}, status=404)

        return HttpResponse({'seller_create_success': "Seller created successfully"}, status=200)

    return HttpResponse({"seller_create_failure": "Seller created failed"}, status=404)



# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
def sellerDelete(request):
    seller_object = Seller.objects.filter(pk=request.GET['pk'])
    seller_object.delete()
    return HttpResponse({"seller_delete_success": "Seller deleted successfully"}, status=200)



# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
def sellerUpdate(request):
    updatedSeller = Seller.objects(id = request.POST['id'])
    updatedSeller.company = request.POST['company'] if request.POST['company'] else updatedSeller.company
    updatedSeller.save()
    return


# @route   GET views.adGet
# @desc    render individual ad
# @access  Public
def sellerGet(request):
    data = serializers.serialize("json", Seller.objects.all())
    return HttpResponse(data)




def usersGet(request):
    data = serializers.serialize("json", User.objects.all())
    return HttpResponse(data)



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
