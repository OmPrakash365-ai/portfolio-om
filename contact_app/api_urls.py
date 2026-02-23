from django.urls import path
from .api_views import contact_api

urlpatterns = [
    path('contact/', contact_api),
]