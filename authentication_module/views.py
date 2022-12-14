from django.shortcuts import render, redirect, reverse
from django.core.files.storage import FileSystemStorage
from photographer.models import *
from .models import *


def register_photographer(request):
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
        bio = request.POST['bio']
        photo = request.FILES['image_select']

        new_photographer = Photographer(name=name, email=email, phone=phone, address=address, age=age, sex=sex, bio=bio, photo=photo)
        new_photographer.save()

        usertype = UserType.objects.get(type='photographer')

        new_user = User(user_type=usertype, username=phone, password=password1, actual_id=new_photographer.id)
        new_user.save()

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

        new_customer = Customer(name=name, email=email, age=age, address=address, sex=sex, phone=phone)
        new_customer.save()

        usertype = UserType.objects.get(type='customer')

        new_user = User(user_type=usertype, username=phone, password=password1, actual_id=new_customer.id)
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
            print('testing on terminal')
            if usertype.type == 'customer' and user.password == password:
                create_session(request, username)
                print("redirecting to customer homepage")
                return redirect(reverse('customer:home'))
            elif usertype.type == 'photographer' and user.password == password:
                create_session(request, username)
                print('redirecting to photographer homepage')
                return redirect(reverse('photographer:home'))

        else:
            return redirect(reverse('authentication_module:login'))

    elif 'phone' in request.session:
        if Customer.objects.filter(phone=request.session['phone']).exists():
            return redirect(reverse('customer:home'))
        else:
            return redirect(reverse('photographer:home'))
    return render(request, 'authentication/login.html')



def create_session(request, phone_num):
    request.session['phone'] = phone_num
    print('new session created')

def delete_session(request):
    request.session.flush()
    request.session.clear_expired()

def logout(request):
    print('sessions deleted')
    delete_session(request)
    return redirect(reverse('authentication_module:login'))