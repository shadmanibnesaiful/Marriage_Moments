from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import authentication_module
import customer.views
from . import views
import photographer.views
app_name = 'customer'

urlpatterns = [
    path('', views.home, name='home'),
    path('book-photographer/<slug:id>', customer.views.book_photographer, name='book-photographer'),

]
