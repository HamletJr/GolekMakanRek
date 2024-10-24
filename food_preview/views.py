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
