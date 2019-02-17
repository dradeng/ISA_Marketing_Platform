from django.shortcuts import render
from django.http import HttpResponse
from .models import Ad, Seller, Buyer
from django.template import loader

def home(request):
    context = {

    }
    template = loader.get_template('base.html')
    return HttpResponse(template.render(context, request))
