from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post


def post(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'title': 'Posts', 'posts': posts})


def create(request: HttpRequest) -> HttpResponseRedirect | HttpResponse | None:
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['title'])
            post.save()
            return redirect('post-list')
        else:
            return render(request, 'posts/create_post.html', {'error': 'Все поля обязательные'})

    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about.html', {'title': 'About us'})


def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/login.html', {'title': 'Login'})
