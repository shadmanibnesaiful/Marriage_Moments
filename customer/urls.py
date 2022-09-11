from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import authentication_module
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.home, name='home'),
]
