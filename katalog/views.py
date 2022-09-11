from django.shortcuts import render
from katalog.models import *

# TODO: Create your views here.

def katalog(request):

    katalog = CatalogItem.objects.all()

    data = {
        'name': "Nicholas Sidharta",
        'id': "2106752294",
        'list': katalog
    }

    return render(request, 'katalog.html', data)