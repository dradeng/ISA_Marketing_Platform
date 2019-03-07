from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
from urllib.error import HTTPError
# Create your views here.

# Create your views here.

def home(request):
    req = urllib.request.Request('http://models-api:8000/api/v1/ads')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(resp_json, status=200)

def ad_detail(request, ad_id):
    reqUrl = 'http://experiences-api:8000/api/v1/ads/' + str(ad_id) + '/ad_detail'
    req = urllib.request.Request('http://models-api:8000/api/v1/ad/<int:{{ad_id}}>/detail')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return HttpResponse(resp_json, status=200)
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(e.args)

def create_user(request):
    print('WHAT UP0')
    if request.method == "GET":
        return HttpResponse(json.dumps({}), status=200)

    elif request.method == "POST":
        post_data = request.POST

        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        print('WHAT UP1')
        req = urllib.request.Request('http://models-api:8000/api/v1/user/create', data=post_encoded, method='POST')
        print('WHAT UP2')
        try:
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        except HTTPError as e:
            return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
        except Exception as e:
            return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
        return HttpResponse(resp_json, status=201)
    else:
        return HttpResponse(json.dumps({"error":"incorrect method (use GET or POST instead)"}), status=405)


def login(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)

    try:
        email = request.POST["email"]
        password = request.POST["password"]
    except KeyError as e:
        return HttpResponse(json.dumps({"error": "Key not found: " + e.args[0]}), status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    post_data = {'email': email, 'password': password}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/login', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(resp_json, status=200)

#******************************************************

def ad_create(request):
    print("hi from experiences")
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)

    try:
        site_title = request.POST['site_title']
        url = request.POST['url']
        cost = request.POST['cost']
        duration = request.POST['duration']
        print(url)
    except KeyError as e:
        return HttpResponse(json.dumps({"error": "Key not found: " + e.args[0]}), status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)


    post_data = {
        'site_title': site_title,
        'url': url,
        'cost': cost,
        'duration': duration,
    }
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    #print(post_encoded)
    req = urllib.request.Request('http://models-api:8000/api/v1/ad/create/', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(resp_json, status=200)

#******************************************************

def check_authenticator(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)

    try:
        auth = request.POST["authenticator"]
    except KeyError as e:
        return HttpResponse(json.dumps({"error": "Key not found: " + e.args[0]}), status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    post_data = {'authenticator': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/check_authenticator', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(resp_json, status=urllib.request.urlopen(req).getcode())

def logout(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"error":"incorrect method (use POST instead)"}), status=405)

    try:
        auth = request.POST["authenticator"]
    except KeyError as e:
        return HttpResponse(json.dumps({"error": "Key not found: " + e.args[0]}), status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    post_data = {'authenticator': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/logout', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(resp_json, status=200)
