from django.shortcuts import render, get_object_or_404
from .models import Post


def posts_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "posts/posts_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "posts/post_detail.html", {"post": post})
