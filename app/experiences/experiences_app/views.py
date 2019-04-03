from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
from urllib.error import HTTPError
from django.http import JsonResponse
from kafka import KafkaProducer
from elasticsearch import Elasticsearch
# Create your views here.

# Create your views here.

def home(request):
    req = urllib.request.Request('http://models-api:8000/api/v1/ads/')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(resp_json)

    except HTTPError as e:
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)
    return JsonResponse(data, safe=False, status=200)

def ad_detail(request, ad_id):

    req = urllib.request.Request('http://models-api:8000/api/v1/ad/' + str(ad_id) + '/ad_detail/')
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    except HTTPError as e:
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)

    if resp_json == "ads":
        return JsonResponse({"error": "Ad not found"},status=404)

    data = json.loads(resp_json)
    return JsonResponse(data, safe=False, status=200)
    #return HttpResponse(json.dumps(ad_list), status=200)

def create_user(request):

    if request.method == "GET":
        return JsonResponse({"error": "Wront HTTP request"}, status=e.code)

    elif request.method == "POST":
        post_data = request.POST

        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')

        req = urllib.request.Request('http://models-api:8000/api/v1/user/create/', data=post_encoded, method='POST')

        try:
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            data = json.loads(resp_json)
        except HTTPError as e:
            return JsonResponse({"error": e.msg}, status=e.code)
        except Exception as e:
            return JsonResponse({"error": str(type(e))}, status=500)
        return JsonResponse(data, status=201)
    else:
        return JsonResponse({"error":"incorrect method (use GET or POST instead)"}, status=405)


def login(request):
    if request.method != "POST":
        return JsonResponse({"error":"incorrect method (use POST instead)"}, status=405)

    try:
        email = request.POST["email"]
        password = request.POST["password"]
    except KeyError as e:
        return JsonResponse({"error": "Key not found: " + e.args[0]}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)

    post_data = {'email': email, 'password': password}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/login', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(resp_json)
    except HTTPError as e:
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)
    return JsonResponse(data, status=200)

#******************************************************

def ad_create(request):
    if request.method != "POST":
        return JsonResponse({"error":"incorrect method (use POST instead)"}, status=405)

    try:
        site_title = request.POST['site_title']
        url = request.POST['url']
        cost = request.POST['cost']
        duration = request.POST['duration']

    except KeyError as e:
        return JsonResponse({"error": "Key not found: " + e.args[0]}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)


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

        data = json.loads(resp_json)
    except HTTPError as e:
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    producer.send('new-listings-topic', resp_json.encode('utf-8'))
    return JsonResponse(data, status=200)

#******************************************************

def check_authenticator(request):
    if request.method != "POST":
        return JsonResponse({"error":"incorrect method (use POST instead)"}, status=405)

    try:
        auth = request.POST["authenticator"]
    except KeyError as e:
        return JsonResponse({"error": "Key not found: " + e.args[0]}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)

    post_data = {'authenticator': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/check_authenticator', data=post_encoded, method='POST')

    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(resp_json)
    except HTTPError as e:
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)
    return JsonResponse(data, status=urllib.request.urlopen(req).getcode())

def logout(request):
    if request.method != "POST":
        return JsonResponse({"error":"incorrect method (use POST instead)"}, status=405)

    try:
        auth = request.POST["authenticator"]
    except KeyError as e:
        return JsonResponse({"error": "Key not found: " + e.args[0]}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)

    post_data = {'authenticator': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/logout', data=post_encoded, method='POST')


    try:
        resp_json = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    except HTTPError as e:
        return JsonResponse({"error": e.msg}, status=e.code)
    except Exception as e:
        return JsonResponse({"error": str(type(e))}, status=500)
    return JsonResponse(resp_json, status=200,safe=False)



def search(request):
    if request.method == "POST":
        return JsonResponse({"error": "incorrect method -> should be GET not POST"}, status=200)

    elif request.method == "GET":
        query = request.GET.get('query', 'none')

        es = Elasticsearch(['es'])

        result = es.search(index='listing_index', body={'query': {'query_string': {'query': query}}, 'size': 5})

        if result['timed_out'] == True:
            return JsonResponse({"error":"Search timed out"}, status=500)

        sources = []
        for returned in result['hits']['hits']:
            sources.append(returned['_source'])

        return JsonResponse(json.dumps(sources), status=201)

    else:
        return JsonResponse({"error":"incorrect method (use GET or POST instead)"}, status=405)
