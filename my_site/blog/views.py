from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post, Author, Tag
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class StartPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ["-date"]
    context_object_name = "posts"


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(
            request,
            "blog/post_detail.html",
            {
                "identified_post": post,
                "tags": post.tags.all(),
                "comment_form": CommentForm(),
                "comments": post.comments.all().order_by("-created_at"),
            },
        )

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))

        return render(
            request,
            "blog/post_detail.html",
            {
                "identified_post": post,
                "tags": post.tags.all(),
                "comment_form": comment_form,
            },
        )
