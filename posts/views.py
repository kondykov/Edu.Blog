from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from posts.models import Post


def post(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'title': 'Posts', 'posts': posts})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about.html',{'title': 'About us'})


def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/login.html',{'title': 'Login'})
