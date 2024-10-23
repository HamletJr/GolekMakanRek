from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'), 
    path('logout/', views.logout_user, name='logout'),
    path('add-restaurant/', views.add_restaurant, name='add_restaurant'),
    path('add-food/', views.add_food, name='add_food'),
    path('add-rating/<uuid:food_id>/', views.add_rating, name='add_rating'),
]