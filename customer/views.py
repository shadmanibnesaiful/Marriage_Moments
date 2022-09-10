from django.shortcuts import render

from photographer.models import *


def home_page(request):
    customer = Customer.objects.get(id=1)

    photographers = Photographer.objects.all()

    context = {
        'photographers' : photographers
    }

    return render(request, 'customer/home.html', context)
