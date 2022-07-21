from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]
