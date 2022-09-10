from django.shortcuts import render

from photographer.models import *


def home_page(request):
    customer = Customer.objects.get(id=1)
    # logical code

    # dictionary

    # render paerge and send dictionary
    return render(request, 'customer/home.html')
