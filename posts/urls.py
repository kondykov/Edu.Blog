from django.urls import path

from posts import views

urlpatterns = [
    path('post/', views.post, name='post-list'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
]