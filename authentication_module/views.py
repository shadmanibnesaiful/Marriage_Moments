from django.shortcuts import render

from photographer.models import *
from .models import *

def load_test(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        #password1 = request.POST['password1']
        #password2 = request.POST['password2']
        address = request.POST['address']
        age = request.POST['age']
        sex = request.POST['sex']
        bio = request.POST['bio']

        new_photographer = Photographer(name=name, email=email, phone=phone, address=address, age=age, sex=sex, bio=bio)

        new_photographer.save()


    return render(request, 'photographer_details/photographer_signup.html')
def register_customer(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        #password1 = request.POST['password1']
        # password2 = request.POST['password2']
        address = request.POST['address']
        age = request.POST['age']
        sex = request.POST['sex']

        new_customer = Customer(name=name, email=email, age=age, address=address, sex=sex)
        new_customer.save()

    return render(request, 'customer_details/customer_signup.html')

def login(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST['email']
        password1 = request.POST['password1']


    return render(request, 'login_page/login_page.html')