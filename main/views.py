from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

def show_main(request):
    context = {
        'features': [
            {'title': 'Discover Culinary Delights'},
            {'title': 'User-Friendly Experience'},
            {'title': 'Local Insights and Recommendations'},
        ],
        'categories': [
            {'name': 'Lontong Balap', 'color': 'green', 'image': '../../static/img/homepage/lontongbalap.jpg'},
            {'name': 'Rujak Cingur', 'color': 'orange', 'image': '../../static/img/homepage/rujakcingur.jpg'},
            {'name': 'Sego Sambel', 'color': 'yellow', 'image': '../../static/img/homepage/segosambel.jpg'},
        ],
        'services': [
            {'title': 'Curated Food Listings', 'description': 'We handpick the best eateries and food stalls in Surabaya, ensuring you always have access to the tastiest and most authentic dishes the city has to offer.', 'icon': '../../static/img/homepage/ap.avif'},
            {'title': 'Up-to-Date Information', 'description': 'Stay informed with the latest updates, including menus, pricing, and operating hours, so you can plan your food adventures without any surprises.', 'icon': '../../static/img/homepage/pl.jpg'},
            {'title': 'Community Feedback', 'description': 'Benefit from real reviews and ratings by fellow food enthusiasts, helping you make informed decisions on where to eat.', 'icon': '../../static/img/homepage/feedback.png'},
        ],
        'special_offer': {'price': 28, 'image': 'images/burger.jpg'},
        'additional_offers': [
            {'title': 'Special Dessert', 'discount': 'Save 20%', 'price': 21, 'color': 'brown'},
            {'title': 'Tortilla wrap tacos', 'discount': '$12 off', 'price': 18, 'color': 'orange'},
        ],
    }
    return render(request, 'main.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('main:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response