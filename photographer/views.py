from django.shortcuts import render


# Create your views here.


def load_test(request):

    # logical code

    # dictionary
    context = {
        'name': 'Rashid',
        'age' : 25
    }

    # render paerge and send dictionary
    return render(request, 'photographer/dashboard.html', context)
