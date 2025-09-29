from django.contrib.auth import views as auth_views
from django.urls import path

from posts import views

urlpatterns = [
    path('post/', views.post, name='post-list'),
    path('post/create', views.create, name='post-create'),
    path('post/<int:post_id>/update', views.update, name='post-update'),
    path('post/<int:post_id>/delete', views.update, name='post-delete'),
    path('post/<int:post_id>/', views.show, name='post-show'),
    path('about/', views.about, name='about'),

    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('profile/', views.profile, name='login'),
    path('logout/', views.sing_out, name='logout'),

]
