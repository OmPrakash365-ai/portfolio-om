from django.urls import path
from . import views


urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/edit/', views.project_update, name='project_update'),
    path('<slug:slug>/delete/', views.project_delete, name='project_delete'),


]

