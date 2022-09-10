from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def load_test(request):
    customer = Customer.objects.get(id=1)
    # logical code

    # dictionary
    context = {
        'name': 'Rashid',
        'age': 25,
        'customer': customer
    }

    # render paerge and send dictionary
    return render(request, 'photographer/photographer_details.html', context)


def photographer_details(request, id):
    print('this function called')
    print(id)

    photographer = Photographer.objects.get(id=id)

    context = {
        'photographer': photographer,
    }

    return render(request, 'photographer/photographer_details.html', context)
