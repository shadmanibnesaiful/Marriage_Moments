from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import *


# Create your views here.

def home(request):
    if 'phone' not in request.session:
        return redirect(reverse('authentication_module:login'))
    else:
        photographer = Photographer.objects.get(phone=request.session['phone'])
        context = {
            'photographer': photographer,
            'orders': Order.objects.filter(package__photographer=photographer),
            'packages': Photography_Package.objects.filter(photographer=photographer),
        }
        return render(request, 'photographer/dashboard.html', context)


def photographer_details(request, id):
    if 'phone' not in request.session:
        return redirect(reverse('authentication_module:login'))
    else:
        print('this function called')
        print(id)

        photographer = Photographer.objects.get(id=id)

        print("------------")
        print(Photography_Package.objects.filter(photographer=photographer))

        context = {
            'photographer': photographer,
            'portfolio_photos': Portfolio.objects.filter(photographer=photographer),
            'packages': Photography_Package.objects.filter(photographer=photographer),
        }
        return render(request, 'photographer/photographer_details.html', context)


def add_portfolio_photo(request):
    if 'phone' not in request.session:
        return redirect(reverse('authentication_module:login'))
    else:
        photo = request.FILES['photo']
        caption = request.POST['caption']

        # fetch from session cookie
        photographer = Photographer.objects.get(phone=request.session['phone'])

        portfolio = Portfolio(photographer=photographer, caption=caption, photo=photo)
        portfolio.save()

        return redirect(reverse('photographer:home'))


def add_photography_package(request):
    if request.method == "POST":
        name = request.POST['package_name']
        desc = request.POST['package_desc']
        fee = request.POST['fee']

        photographer = Photographer.objects.get(phone=request.session['phone'])

        package = Photography_Package(photographer=photographer, name=name, fee=fee, description=desc)
        package.save()

        return redirect(reverse('photographer:home'))


def delete_package(request):
    if request.method == "POST":
        id = request.POST['package_id']

        package = Photography_Package.objects.get(id=id)
        package.delete()

        print('package deleted')

    return redirect(reverse('photographer:home'))


def update_bio(request):
    if request.method == 'POST':
        bio = request.POST['bio']

        photographer = Photographer.objects.get(phone=request.session['phone'])
        photographer.bio = bio

        photographer.save()


    return redirect(reverse('photographer:home'))