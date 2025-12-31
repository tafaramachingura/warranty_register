# warranty_api/urls.py
from django.urls import path
from .views import register_warranty

urlpatterns = [
    path('register-warranty/', register_warranty, name='register-warranty'),
]
