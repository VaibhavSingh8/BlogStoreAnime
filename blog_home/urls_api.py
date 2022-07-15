from django.contrib import admin
from django.urls import path
from . import views_api

urlpatterns = [
        path('login/', views_api.loginUser),
        path('signup/', views_api.registerUser),
]