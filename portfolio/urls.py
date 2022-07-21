from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.main, name='main'),
]
