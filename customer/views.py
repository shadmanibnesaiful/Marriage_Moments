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
            'photographers': photographers
        }

        return render(request, 'customer/home.html', context)


def book_photographer(request):
    print(f"book photographer confirmed {id}")

    if request.method == 'POST':
        package_id = request.POST['package_id']

        customer = Customer.objects.get(phone=request.session['phone'])
        photography_package = Photography_Package.objects.get(id=package_id)

        order = Order(customer=customer, package=photography_package, date=datetime.today())
        order.save()

    return redirect(reverse('customer:home'))
