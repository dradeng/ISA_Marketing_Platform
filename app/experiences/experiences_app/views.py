from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
from urllib.error import HTTPError
# Create your views here.

# Create your views here.

def home(request):
    req = urllib.request.Request('http://models-api:8000/api/v1/ad')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(resp_json, status=200)

def ad_detail(request, ad_id):
    reqUrl = 'http://experiences-api:8000/api/v1/ad/' + str(ad_id) + '/ad_detail'
    req = urllib.request.Request('http://models-api:8000/api/v1/ad/<int:{{ad_id}}>/detail')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return HttpResponse(resp_json, status=200)
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(e.args)

def create_user(request):
    if request.method == "GET":
        return HttpResponse(json.dumps({}), status=200)

    elif request.method == "POST":
        post_data = request.POST

        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/api/v1/user/create', data=post_encoded, method='POST')

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
        username = request.POST["username"]
        password = request.POST["password"]
    except KeyError as e:
        return HttpResponse(json.dumps({"error": "Key not found: " + e.args[0]}), status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)

    post_data = {'username': username, 'password': password}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/login', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)
    return HttpResponse(resp_json, status=200)

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
