from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from urllib.error import HTTPError
from .forms import LoginForm, MarketUserForm, adCreateForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import urllib.request
import json
import ast
from django.http import JsonResponse

# @route   Get views.home
# @desc    Render home page
# @access  Private
def home(request):
    auth = user_logged_in(request)

    req = urllib.request.Request('http://experiences-api:8000/api/v1/home')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(resp_json)

        return render(request, 'home.html',{'ads': data, 'auth':auth })
    except HTTPError as e:
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": "Exception"}, status=500)


# @route   GET views.userCreate
# @desc    return ad info
# @access  Public
def ad_detail(request, ad_id):
    reqUrl = 'http://experiences-api:8000/api/v1/ad/' + str(ad_id) + '/ad_detail'
    req = urllib.request.Request(reqUrl)

    reqRec = urllib.request.Request('http://exp-api:8000/api/v1/recommend/' + str(ad_id))

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        req1.add_header("Cookie", "auth="+auth_cookie)
    except HTTPError as e:
        return JsonResponse({"error":"Ad ID not found"}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)

    ad = json.loads(resp_json)
    #if 'error' in ad.keys():
        #return render(request, 'ad_detail.html',{'ad': })


    try:
        resp_json1 = urllib.request.urlopen(reqRec).read().decode('utf-8')
    except HTTPError as e:
        return JsonResponse({"error":"Whatup Sai"}, status=e.code)

    recs = json.loads(resp_json1)
    return render(request, 'ad_detail.html',{'ad': ad, "recs":recs})


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
    auth = user_logged_in(request)
    print('AUTH IS', auth)
    if(auth):
        #doesnt allow user to login if authenticator is good
        HttpResponseRedirect("/")

    print("WE CALL")
    if request.method == 'GET':
        print("we in here")
        auth = user_logged_in(request)
        form = LoginForm()
        context = {"form": form, "auth": auth}

        print(auth)
        return render(request, "login.html", context)
    if request.method == "POST":
        print('WE HERE MOTH')

    f = LoginForm(request.POST)
    print("WE MADE IT")
    # Check if the form instance is invalid
    if not f.is_valid():
      context = {"form": f, "error": "Form was invalid"}
      return render(request, 'login.html', context)


    email = f.cleaned_data['email']
    password = f.cleaned_data['password']
    print("EMAIL IT IS")
    print(email)
    post_data = {'email': email, 'password': password}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    print('bout to call experiences')
    req = urllib.request.Request('http://experiences-api:8000/api/v1/login', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        print('RESPONSE', resp_json)
    except HTTPError as e:
        print('ERROR msg', e.msg)
        context = {"form": f, "error": "HTTP error: " + e.msg}
        return render(request, 'login.html', context)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)

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
        return JsonResponse({"error": str(type(e))}, status=500)

    return HttpResponseRedirect("/")

#*************************************************
@login_required
def ad_create(request):
    if request.method == 'GET':
        auth = user_logged_in(request)
        form = adCreateForm()
        context = {"form": form, "auth": auth}
        return render(request, "ad_create.html", context)

    f = adCreateForm(request.POST)
    print(f.errors)

    # Check if the form instance is invalid
    if not f.is_valid():
      context = {"form": f, "error": "Form was invalid"}
      return render(request, 'ad_create.html', context)


    site_title = f.cleaned_data['site_title']
    url = f.cleaned_data['url']
    cost = f.cleaned_data['price']
    duration = f.cleaned_data['duration']

    post_data = {
        'site_title': site_title,
        'url': url,
        'cost': cost,
        'duration': duration,
    }

    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://experiences-api:8000/api/v1/ad_create', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        print("oof")
        return JsonResponse({"error": str(type(e))}, status=500)

    return redirect("/")
#*************************************************



def get_user_object(request):
    auth = request.COOKIES.get('auth')
    post_data = {'authenticator': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://experiences-api:8000/api/v1/check_authenticator', data=post_encoded, method='POST')

    try:
        response = urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        return {}
    response_dict = json.loads(response)
    user_dict = {}
    user_dict['id'] = response_dict['user_id']
    return user_dict


@csrf_exempt
def create_account(request):
    print('we outside')
    auth = user_logged_in(request)
    form = MarketUserForm()


    if request.method == "GET":
        context = {"form": form, "auth": auth, "error": ""}
        return render(request, "create_account.html", context)
    elif request.method == "POST":
        print('we inside')
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
            context = {"form": form, "auth": auth, "error": "Email already in use"}
            return render(request, "create_account.html", context)
        except Exception as e:
            return JsonResponse({"error": str(type(e))}, status=500)
        return redirect("home")

def search(request):
    auth = user_logged_in(request)
    query = request.GET.get('query')
    req = urllib.request.Request('http://experiences-api:8000/api/v1/search?query='+urllib.parse.quote(query))
    try:
        print('madeee')

        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        print('goolla')
    except HTTPError as e:
        print('http')
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        print('exception')
        return JsonResponse({"error": str(type(e))}, status=500)
    print('weird')
    ads = json.loads(resp_json)
    print('made it here')
    return render(request, "search.html", {"ads":ads, "auth":auth, "results": len(ads)})
