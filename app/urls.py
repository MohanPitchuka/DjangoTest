from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('get-date/' , views.get_date, name='get-date')
]
