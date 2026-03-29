from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Profile
from projects_app.models import Project
import requests

# 🔒 ADMIN CHECK
def is_admin(user):
    return user.is_superuser


# 🏠 HOME
def home(request):
    return render(request, 'home.html')


# 🔐 SIGNUP
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # validation
        if password != confirm_password:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})

        if len(password) < 6:
            return render(request, 'accounts/signup.html', {'error': 'Password must be at least 6 characters'})

        if User.objects.filter(username=email).exists():
            return render(request, 'accounts/signup.html', {'error': 'User already exists'})

        # create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        login(request, user)
        return redirect('dashboard')

    return render(request, 'accounts/signup.html')


# 🔐 LOGIN (NORMAL USER)
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


# 🔓 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# 🔐 DASHBOARD LOGIN (ADMIN ONLY)
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/dashboard.html', {'error': 'Invalid admin credentials'})

    return render(request, 'accounts/dashboard.html')


# 📊 DASHBOARD (ADMIN ONLY)

def dashboard(request):
    projects = Project.objects.all().order_by('-created_date')

    return render(request, 'accounts/dashboard.html',{'projects': projects})


# ℹ️ ABOUT PAGE
def about(request):
    return render(request, 'accounts/about.html')



def education(request):
    return render(request, 'education.html')

def skills(request):
    return render(request, 'skills.html')


def achievements(request):
    context = {
        "total_solved": 150,   # update manually
        "easy": 70,
        "medium": 50,
        "hard": 30
    }
    return render(request, "achievements.html", context)

def certificates(request):
    return render(request, 'certificates.html')

def internships(request):
    return render(request, 'internships.html')

def hackathons(request):
    return render(request, 'hackathons.html')