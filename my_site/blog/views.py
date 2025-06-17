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
    
    def is_stored(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        is_saved = None
        if stored_posts is not None:
            is_saved = post.id in stored_posts
        else:
            is_saved = False

        return is_saved

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        is_saved = self.is_stored(request, post.id)

        return render(
            request,
            "blog/post_detail.html",
            {
                "identified_post": post,
                "tags": post.tags.all(),
                "comment_form": CommentForm(),
                "comments": post.comments.all().order_by("-created_at"),
                "saved_for_later": is_saved,
                
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
                 "saved_for_later": self.is_stored(request, post.id),
            },
        )


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["has_posts"] = False
            context["posts"] = []

        else:
            context["has_posts"] = True
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts

        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        if request.POST["post_id"] not in stored_posts:
            stored_posts.append(int(request.POST["post_id"]))
                  
        else:
            stored_posts.remove(int(request.POST["post_id"]))
            
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
