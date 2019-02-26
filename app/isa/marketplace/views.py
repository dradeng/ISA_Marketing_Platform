from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Seller, Buyer, Ad, MarketUser
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import AdForm
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
@csrf_exempt
def adCreate(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('user')
            image = request.GET.get('image')
            cost = request.GET.get('cost')
            duration = request.GET.get('duration')
            url =request.GET.get('url')
            site_title = reques.GET.get('site_title')
            user = MarketUser.objects.get(pk=user_id)
            createdAd = Buyer(user=user, image=image, cost=cost, duration=duration,site_title=site_title, url=url)
            createdAd.save()
        except:
            return HttpResponse({'ad_create_failure': "User does not exist"}, status=404)

        return HttpResponse({'ad_create_success': "Ad created successfully"}, status=200)

    return HttpResponse({"ad_create_failure": "Ad created failed"}, status=404)



# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
def adDelete(request):
    if request.method == "DELETE":
        try:
            ad_object = Ad.objects.get(pk=request.GET['pk'])
            ad_object.delete()
            return HttpResponse({"ad_delete_success": "Ad deleted successfully"}, status=200)
        except:
            return HttpResponse({"seller_delete_failure": "Ad could not be ound"}, status=404)
    return HttpResponse({"seller_delete_failure": "Invalid Method Request"}, status=404)


# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
@csrf_exempt
def adUpdate(request):
    if request.method == "POST":
        try:
            ad_id = request.GET.get('pk')
            updatedAd = Ad.objects.get(pk=ad_id)
            updatedAd.image = request.GET.get('image') if request.GET.get('image') else updatedAd.image
            updatedAd.duration = request.GET.get('duration') if request.GET.get('duration') else updatedAd.duration
            updatedAd.cost = request.GET.get('cost') if request.GET.get('cost') else updatedAd.cost
            updatedAd.url = request.GET.get('url') if request.GET.get('url') else updatedAd.url
            updatedAd.site_title = request.GET.get('site_title') if request.GET.get('site_title') else updatedAd.site_title
            updatedAd.save()
            updatedAd.save()
            return HttpResponse({"ad_update_success": "Ad Updated successfully"}, status=200)
        except:
            return HttpResponse({"ad_update_failure": "Ad unable to find"}, status=404)

    return HttpResponse({'ad_update_failure': "Invalid Request"}, status=404)

# @route   GET views.adGet
# @desc    render all ad
# @access  Public
def adGet(request):
    if request.method == "GET":
        data = serializers.serialize("json", Ad.objects.all())
        return HttpResponse(data)
    return HttpResponse({'ad_get_failure': "Invalid Request"}, status=404)

def ad_detail(request, ad_id):
    data = serializers.serialize("json", Ad.objects.get(pk=ad_id))
    return HttpResponse(ad)


# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
@csrf_exempt
def buyerCreate(request):
    if request.method == "POST":
        try:
            user_id=request.GET.get('user')
            credit=request.GET.get('credit')
            user = MarketUser.objects.get(pk=user_id)
            createdBuyer = Buyer(user=user, credit=credit)
            createdBuyer.save()
        except:
            return HttpResponse({'buyer_create_failure': "User does not exist"}, status=404)

        return HttpResponse({'buyer_create_success': "Buyer created successfully"}, status=200)

    return HttpResponse({"buyer_create_failure": "Buyer created failed"}, status=404)



# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
@csrf_exempt
def buyerDelete(request):
    if request.method == "DELETE":
        try:
            buyer_object = Buyer.objects.get(pk=request.GET['pk'])
            buyer_object.delete()
            return HttpResponse({"buyer_delete_success": "Buyer deleted successfully"}, status=200)
        except:
            return HttpResponse({"buyer_delete_failure": "Buyer could not be found"}, status=404)
    return HttpResponse({"seller_delete_failure": "Invalid Method Request"}, status=404)


# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
@csrf_exempt
def buyerUpdate(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('pk')
            updatedBuyer = Buyer.objects.get(pk=user_id)
            updatedBuyer.company = request.GET.get('credit') if request.GET.get('credit') else updatedBuyer.credit
            updatedBuyer.save()
            return HttpResponse({"buyer_update_success": "Buyer Updated successfully"}, status=200)
        except:
            return HttpResponse({"buyer_update_failure": "Missing params or user not found"}, status=404)
    return HttpResponse({'seller_update_failure': "Invalid Request"}, status=404)


# @route   GET views.adGet
# @desc    render individual ad
# @access  Public
def buyerGet(request):
    if request.method == "GET":
        data = serializers.serialize("json", Buyer.objects.all())
        return HttpResponse(data)
    return HttpResponse({'buyer_get': "Invalid request"}, status=404)

# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
@csrf_exempt
def sellerCreate(request):
    if request.method == "POST":
        try:
            user_id=request.GET.get('user')
            company=request.GET.get('company')
            user = MarketUser.objects.get(pk=user_id)
            createdSeller = Seller(user=user, company=company)
            createdSeller.save()
        except:
            return HttpResponse({'seller_create_failure': "User does not exist"}, status=404)

        return HttpResponse({'seller_create_success': "Seller created successfully"}, status=200)

    return HttpResponse({"seller_create_failure": "Seller created failed"}, status=404)



# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
@csrf_exempt
def sellerDelete(request):
    if request.method == "DELETE":
        try:
            seller_object = Seller.objects.get(pk=request.GET['pk'])
            seller_object.delete()
            return HttpResponse({"seller_delete_success": "Seller deleted successfully"}, status=200)
        except:
            return HttpResponse({"seller_delete_failure": "Seller could not be found"}, status=404)
    return HttpResponse({"seller_delete_failure": "Invalid Method Request"}, status=404)



# @route   POST views.adUpdate
# @desc    Update an ad
# @access  Private
@csrf_exempt
def sellerUpdate(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('pk')
            updatedSeller = Seller.objects.get(pk=user_id)
            updatedSeller.company = request.GET.get('company') if request.GET.get('company') else updatedSeller.company
            updatedSeller.save()
            return HttpResponse({"seller_update_success": "Seller Updated successfully"}, status=200)
        except:
            return HttpResponse({"seller_update_failure": "Missing params or user not found"}, status=404)

    return HttpResponse({'seller_update_failure': "Invalid Request"}, status=404)




# @route   GET views.adGet
# @desc    render individual ad
# @access  Public
def sellerGet(request):
    if request.method == "GET":
        data = serializers.serialize("json", Seller.objects.all())
        return HttpResponse(data)
    return HttpResponse({'seller_get': "Invalid Request"}, status=404)




def usersGet(request):
    data = serializers.serialize("json", MarketUser.objects.all())
    return HttpResponse(data)
