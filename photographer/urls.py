from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import authentication_module.views
import photographer.views

app_name = 'photographer'

urlpatterns = [
    path('', photographer.views.home, name='home'),
    path('details/<slug:id>/', photographer.views.photographer_details, name='photographer-details'),
    path('add-photo', photographer.views.add_portfolio_photo, name='add-photo'),
    path('add-package', photographer.views.add_photography_package, name='add-package'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
