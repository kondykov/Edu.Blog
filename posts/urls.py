from django.shortcuts import redirect
from django.urls import path

from posts import views

urlpatterns = [
    path('post/', views.post, name='post-list'),
    path('post/create', views.create, name='post-create'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
]