from django.shortcuts import render, redirect, reverse

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


    return render(request, 'authentication/photographer_signup.html')
def register_customer(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        age = request.POST['age']
        sex = request.POST['sex']

        # #############################
        # add phone number to customer
        # ############################
        new_customer = Customer(name=name, email=email, age=age, address=address, sex=sex, phone=phone)
        new_customer.save()

        usertype = UserType.objects.get(type='customer')

        new_user = User(user_type=usertype, username= phone, password = password1, actual_id=new_customer.id)
        new_user.save()

    return render(request, 'authentication/customer_signup.html')

def login(request):

    if request.method == "POST":
        print(request.POST)

        # username is the phone number of the user
        username = request.POST['username']
        password = request.POST['password']
        print("here it is")

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            usertype = user.user_type

            if usertype.type == 'customer':
                print("redirecting to customer homepage")
                pass
            elif usertype.type == 'photographer':
                print('redirecting to photographer homepage')
                pass

        else:
            return redirect(reverse('authentication_module:login'))

    return render(request, 'authentication/login.html')