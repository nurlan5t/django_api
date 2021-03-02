from django.contrib import admin
from django.urls import path, include
from lesson2 import views

urlpatterns = [
    path('brands/', views.car_brand_list_view),
    path('cars/', views.car_list_view),
]