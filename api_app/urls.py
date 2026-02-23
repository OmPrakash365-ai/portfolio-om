from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list_api),
    path('projects/<slug:slug>/', views.project_detail_api),
    path('projects/create/', views.project_create_api),
    path('contact/', views.contact_api),
]
