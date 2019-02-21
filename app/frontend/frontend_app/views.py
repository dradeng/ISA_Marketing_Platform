from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from urllib.error import HTTPError



# @route   Get views.home
# @desc    Render home page
# @access  Private
def home(request):

    req = urllib.request.Request('http://experience-api:8000/api/v1/home', method="GET")
    try:
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        ad_list = json.load(resp_json)
        return render(request, 'home.html',
            {'ads': ad_list })
    except HTTPError as e:
        return HttpResponse(json.dumps({"error": e.msg}), status=e.code)
    except Exception as e:
        return HttpResponse(json.dumps({"error": str(type(e))}), status=500)


# @route   GET views.userCreate
# @desc    return ad info
# @access  Public
def ad_detail(request, ad_id):

    #ad = get_object_or_404(Ad, pk=ad_id)
    #return render(request, 'ad_detail.html',
    #              {'ad': ad})
    return HttpResponse("return this string2")
