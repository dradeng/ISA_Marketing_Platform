from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Seller, Buyer, Ad,MarketUser, Authenticator
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import AdForm
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password

import json
import hmac


@csrf_exempt
def adCreate(request):
    if request.method == "POSTT":
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




def adDelete(request):
    if request.method == "DELETE":
        try:
            ad_object = Ad.objects.get(pk=request.GET['pk'])
            ad_object.delete()
            return HttpResponse({"ad_delete_success": "Ad deleted successfully"}, status=200)
        except:
            return HttpResponse({"seller_delete_failure": "Ad could not be ound"}, status=404)
    return HttpResponse({"seller_delete_failure": "Invalid Method Request"}, status=404)



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



# @route   POST views.adUpdate
# @desc    Update an user
# @access  Private
@csrf_exempt
def userUpdate(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('pk')
            updatedUser = MarketUser.objects.get(pk=user_id)
            updatedUser.name = request.GET.get('name') if request.GET.get('name') else updatedUser.name
            updatedUser.save()
            return HttpResponse({"user_update_success": "User Updated successfully"}, status=200)
        except:
            return HttpResponse({"user_update_failure": "Missing params or user not found"}, status=404)

    return HttpResponse({'user_update_failure': "Invalid Request"}, status=404)



# @route   DELETE views.adDelete
# @desc    delete ad
# @access  Private
@csrf_exempt
def userDelete(request):
    if request.method == "DELETE":
        try:
            user_object = MarketUser.objects.get(pk=request.GET['pk'])
            user_object.delete()
            return HttpResponse({"user_delete_success": "User deleted successfully"}, status=200)
        except:
            return HttpResponse({"user_delete_failure": "User could not be found"}, status=404)
    return HttpResponse({"user_delete_failure": "Invalid Method Request"}, status=404)


# @route   POST views.adCreate
# @desc    Create an ad
# @access  Private
@csrf_exempt
def userCreate(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)

    try:
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        user_object = MarketUser(name=name, email=email, password=password)
        user_object.save()
    except KeyError as e:
        return HttpResponse(json.dumps({"error": "Key not found: " + e.args[0]}), status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    return HttpResponse(json.dumps(model_to_dict(user_object)), status=201)

def usersGet(request):
    data = serializers.serialize("json", MarketUser.objects.all())
    return HttpResponse(data)


def check_authenticator(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)

    try:
        authenticator = request.POST["authenticator"]
        auth_object = Authenticator.objects.get(authenticator=authenticator)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Not logged in"}), status=401)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(json.dumps({"success": "User logged in", "user_id": auth_object.user.id}), status=200)

def login(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)

    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user_list = MarketUser.objects.filter(username=username)
    except KeyError as e:
        return HttpResponse(json.dumps({"error": "Key not found: " + e.args[0]}), status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    if len(user_list) == 0:
        return HttpResponse(json.dumps({"error": "Credentials invalid"}), status=401)
    elif len(user_list) > 1:
        return HttpResponse(json.dumps({"error": "More than one user has that login"}), status=401)
    else:
        user_object = user_list[0]
    if not check_password(password, user_object.password):
        return HttpResponse(json.dumps({"error": "Credentials invalid"}), status=401)

    authenticator = hmac.new(
        key=settings.SECRET_KEY.encode('utf-8'),
        msg=os.urandom(32),
        digestmod='sha256',
    ).hexdigest()
    try:
        authenticator_object = Authenticator(authenticator=authenticator, user=user_object)
        authenticator_object.save()
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    return HttpResponse(json.dumps({"authenticator": authenticator}), status=200)

def logout(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)
    try:
        authenticator = request.POST["authenticator"]
        auth_object = Authenticator.objects.get(authenticator=authenticator)
        auth_object.delete()
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error": "Not logged in"}), status=401)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(json.dumps({"success": "User logged out"}), status=200)
