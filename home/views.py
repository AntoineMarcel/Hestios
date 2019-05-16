from django.http import HttpResponse, Http404
from django.shortcuts import render
import requests
from home.models import Villes

def my_view(request, endroit):
    test = Villes.objects.get(ville=endroit)
    return render(request, 'home/ville.html', locals())


