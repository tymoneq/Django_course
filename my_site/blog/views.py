from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def post_list(request):
    return render(request, "blog/post_list.html")


def post_detail(request, post_slug):
    return render(request, "blog/post_detail.html", {"post_slug": post_slug})