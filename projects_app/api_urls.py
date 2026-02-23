from django.urls import path
from . import api_views

urlpatterns = [
    path('projects/', api_views.project_list_api),
    path('projects/<slug:slug>/', api_views.project_detail_api),
    path('projects/create/', api_views.project_create_api),
]