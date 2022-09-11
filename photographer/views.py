from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    return render(request, 'photographer/dashboard.html', {})

def photographer_details(request, id):
    print('this function called')
    print(id)

    photographer = Photographer.objects.get(id=id)

    context = {
        'photographer': photographer,
        'portfolio_photos': Portfolio.objects.filter(photographer=photographer),
    }
    return render(request, 'photographer/photographer_details.html', context)
