from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("post", views.post_list, name="post_list"),
    path("post/<slug:post_slug>", views.post_detail, name="post_detail"),
]