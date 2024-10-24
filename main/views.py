from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

@login_required(login_url='/login')
def show_main(request):
    context = {
        'features': [
            {'title': 'Fast delivery', 'description': 'Promise to deliver within 30 mins'},
            {'title': 'Pick up', 'description': 'Pickup delivery at your doorstep'},
            {'title': 'Dine in', 'description': 'Enjoy your food fresh crispy and hot'},
        ],
        'categories': [
            {'name': 'Lontong Balap', 'color': 'green', 'image': '../../static/img/homepage/lontongbalap.jpg'},
            {'name': 'Rujak Cingur', 'color': 'orange', 'image': '../../static/img/homepage/rujakcingur.jpg'},
            {'name': 'Sego Sambel', 'color': 'yellow', 'image': '../../static/img/homepage/segosambel.jpg'},
        ],
        'services': [
            {'title': 'Automated Packaging', 'description': '100% environment friendly packaging', 'icon': '../../static/img/homepage/ap.avif'},
            {'title': 'Packed with Love', 'description': 'We deliver the best experiences', 'icon': '../../static/img/homepage/pl.jpg'},
            {'title': 'Fastest Delivery', 'description': 'Promise to deliver within 30 mins', 'icon': '../../static/img/homepage/fd.webp'},
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