from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post, Author, Tag

# Create your views here.


def index(request):
    latest_posts = Post.objects.order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": all_posts})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/post_detail.html",
        {"slug": slug, "identified_post": identified_post, "tags": identified_post.tags.all()},
    )
