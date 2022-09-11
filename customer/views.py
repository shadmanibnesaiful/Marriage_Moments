from django.shortcuts import render, redirect, reverse

from photographer.models import *


def home(request):
    if 'phone' not in request.session:
        return redirect(reverse('authentication_module:login'))
    else:
        customer = Customer.objects.get(id=1)

        photographers = Photographer.objects.all()

        context = {
            'photographers' : photographers
        }

        return render(request, 'customer/home.html', context)


def book_photographer(request):
    pass