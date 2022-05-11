from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('home/', views.home, name="home"),
]