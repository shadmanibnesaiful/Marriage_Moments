from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import authentication_module.views
import photographer.views

app_name = 'photographer'

urlpatterns = [
    path('details/<slug:id>/', photographer.views.photographer_details, name='photographer-details')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
