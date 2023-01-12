from django.shortcuts import render, redirect 
from django.http.request import HttpRequest
from server.apps.posts.models import Post

# args, keyword args(kwargs)

def hello_world(request, *args, **kwargs):
    return render(request, "posts/hello_world.html")

def posts_list(request, *args, **kwargs):
    posts = Post.objects.all()
    text = request.GET.get('text')
    if text:
        posts = posts.filter(content__contains = text)

    return render(request, "posts/posts_list.html", {"posts":posts})
    # context = template으로 데이터를 전달

def posts_retrieve(request, pk, *args, **kwargs):
    post = Post.objects.all().get(pk=pk)
    return render(request, "posts/posts_retrieve.html", {"post":post})

def posts_create(request, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title = request.POST["title"],
            user = request.POST["user"],
            region = request.POST["region"],
            price = request.POST["price"],
            content = request.POST["content"],
        )
        return redirect("/")
    return render(request, "posts/posts_create.html")

def posts_update(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.user = request.POST["user"]
        post.region = request.POST["region"]
        post.price = request.POST["price"]
        post.content = request.POST["content"]
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/posts_update.html", {"post": post})

def posts_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.delete()
    return redirect("/")