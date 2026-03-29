from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('achievements/', views.achievements, name='achievements'),
    path('certificates/', views.certificates, name='certificates'),
    path('internships/', views.internships, name='internships'),
    path('hackathons/', views.hackathons, name='hackathons'),
]