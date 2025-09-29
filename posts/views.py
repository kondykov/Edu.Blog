from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from posts.forms import PostForm, UserForm
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
            return render(request, 'posts/post.create.html', {'error': 'Все поля обязательные'})

    form = PostForm()
    return render(request, 'posts/post.create.html', {'form': form})


def show(request: HttpRequest, post_id: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post.show.html', {'post': post})

def update(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('post-list')
    else:
        ...
    return render(request, 'posts/post.edit.html', {'post': post})

def delete(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
    return redirect('post-list')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about.html', {'title': 'About us'})

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/profile.html', {'user': request.user})

def sign_in(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('post-list')
            else:
                return render(request, 'posts/login.html', {'errors': 'Неверные имя пользователя и/или пароль'})

    return render(request, 'posts/login.html', {'title': 'Login'})

@login_required
def sing_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')
