
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.project_list),    
]
