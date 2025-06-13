from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]