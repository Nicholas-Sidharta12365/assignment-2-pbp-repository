from django.shortcuts import render
from mywatchlist.models import *
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def mywatchlist(request):

    movies = Watchlist.objects.all()

    data = {
        'name': "Nicholas Sidharta",
        'id': "2106752294",
        'movies': movies
    }

    return render(request, 'mywatchlist.html',data)

def mywatchlist_xml(request):

    data = Watchlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def mywatchlist_json(request):

    data = Watchlist.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")