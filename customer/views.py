from datetime import datetime

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


def book_photographer(request, id):
    print(f"book photographer confirmed {id}")

    customer = Customer.objects.get(phone=request.session['phone'])
    photographer = Photographer.objects.get(id=id)

    order = Order(photographer=photographer, customer=customer, date=datetime.today())
    order.save()

    return redirect(reverse('customer:home'))