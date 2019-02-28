from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from urllib.error import HTTPError
from .forms import LoginForm, MarketUserForm
from django.views.decorators.csrf import csrf_exempt

import urllib.request
import json

# @route   Get views.home
# @desc    Render home page
# @access  Private
def home(request):

    req = urllib.request.Request('http://experiences-api:8000/api/v1/home')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        ad_list = json.loads(resp_json)
        print(ad_list)
        return render(request, 'home.html',{'ads': ad_list })
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(e.args)


# @route   GET views.userCreate
# @desc    return ad info
# @access  Public
def ad_detail(request, ad_id):
    reqUrl = 'http://experiences-api:8000/api/v1/ad/' + str(ad_id) + '/ad_detail'
    req = urllib.request.Request(reqUrl)
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        ad = json.loads(resp_json)
        return render(request, 'ad_detail.html',{'ad': ad})
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(e.args)


###### AUTH STUFF

#Use for create ad, user has to login
#Use for buying an ad
def login_required(f):
    def wrap(request, *args, **kwargs):
        if user_logged_in(request):
            return f(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("login")

    return wrap


def user_logged_in(request):
    auth = request.COOKIES.get('auth')
    post_data = {'authenticator': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://experiences-api:8000/api/v1/check_authenticator', data=post_encoded, method='POST')

    try:
        response = urllib.request.urlopen(req)
    except Exception as e:
        return False
    return True


def login(request):
    if request.method == 'GET':
        auth = user_logged_in(request)
        form = LoginForm()
        context = {"form": form, "auth": auth}
        return render(request, "login.html", context)

    f = LoginForm(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
      context = {"form": f, "error": "Form was invalid"}
      return render(request, 'login.html', context)


    username = f.cleaned_data['username']
    password = f.cleaned_data['password']

    post_data = {'username': username, 'password': password}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://experiences-api:8000/api/v1/login', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        context = {"form": f, "error": "HTTP error: " + e.msg}
        return render(request, 'login.html', context)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    resp_dict = json.loads(resp_json)
    authenticator = resp_dict['authenticator']
    response = HttpResponseRedirect("/")

    response.set_cookie("auth", authenticator)
    return response

@login_required
def logout(request):
    auth = request.COOKIES.get('auth')
    post_data = {'authenticator': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://experiences-api:8000/api/v1/logout', data=post_encoded, method='POST')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    return HttpResponseRedirect("/")

@csrf_exempt
def create_account(request):
    auth = user_logged_in(request)
    if request.method == "GET":
        form = MarketUserForm()
        context = {"form": form, "auth": auth}
        return render(request, "create_account.html", context)
    elif request.method == "POST":
        form = MarketUserForm(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
        else:
            context = {"form": form, "auth": auth, "error": "The form was invalid, please enter valid data"}
            return render(request, "create_account.html", context)

        post_encoded = urllib.parse.urlencode(user_info).encode('utf-8')
        req = urllib.request.Request('http://experiences-api:8000/api/v1/create_user', data=post_encoded, method='POST')
        try:
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        except HTTPError as e:
            return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
        except Exception as e:
            return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
        return redirect("home")
