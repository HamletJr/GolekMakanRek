from django.urls import path
from . import views

app_name = 'food_preview'

urlpatterns = [
    path('add-restaurant/', views.add_restaurant, name='add_restaurant'),
    path('add-food/', views.add_food, name='add_food'),
    path('add-rating/<uuid:food_id>/', views.add_rating, name='add_rating'),
]