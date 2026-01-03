# warranty_core/urls.py
from django.contrib import admin
from django.urls import path, include
from home.views import home
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin/login/', permanent=False)),
    path("api/", include("warranty_api.urls")),
    
]
