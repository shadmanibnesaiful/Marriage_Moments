from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import authentication_module
from . import views

app_name = 'authentication_module'

urlpatterns = [
    path('signup_photographer/', views.register_photographer, name='signup_photographer'),
    path('signup_customer/', views.register_customer, name='signup_customer'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),

]
