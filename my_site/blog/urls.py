from . import views
from django.urls import path

urlpatterns = [
    path("", views.StartPageView.as_view(), name="index"),
    path("post", views.PostListView.as_view(), name="post_list"),
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later"),
]