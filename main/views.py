from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

@login_required(login_url='/login')
def show_main(request):
    if not request.user.is_authenticated:
        return redirect('main:login')
    restaurants = Restaurant.objects.all()
    foods = Food.objects.all().select_related('restoran')
    food_ratings = FoodRating.objects.all().select_related('user', 'deskripsi_food')
    ratings_by_food = {}
    
    for rating in food_ratings:
        food_id = rating.deskripsi_food.id
        if food_id not in ratings_by_food:
            ratings_by_food[food_id] = []
        ratings_by_food[food_id].append(rating)
    context = {
        'restaurants': restaurants,
        'foods': foods,
        'ratings_by_food': ratings_by_food,
        'last_login': request.COOKIES['last_login'] if 'last_login' in request.COOKIES else None,
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

@login_required(login_url='/login')
def add_restaurant(request):
    form = RestaurantForm()
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'add_restaurant.html', context)

@login_required(login_url='/login')
def add_food(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    context = {'form': form}
    return render(request, 'add_food.html', context)

@login_required(login_url='/login')
def add_rating(request, food_id):
    food = Food.objects.get(id=food_id)
    form = FoodRatingForm()
    if request.method == 'POST':
        form = FoodRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.deskripsi_food = food
            rating.save()
            return redirect('main:show_main')
    context = {'form': form, 'food': food}
    return render(request, 'add_rating.html', context)