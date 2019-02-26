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
