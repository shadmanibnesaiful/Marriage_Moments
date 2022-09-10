from django.shortcuts import render
from .models import *

# Create your views here.


def load_test(request):
    customer = Customer.objects.get(id=1)
    # logical code

    # dictionary
    context = {
        'name': 'Rashid',
        'age' : 25,
        'customer' : customer
    }

    # render paerge and send dictionary
    return render(request, 'photographer_details/../templates/photographer/photographer_details.html', context)

