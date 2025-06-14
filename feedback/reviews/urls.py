from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('thank-you/<str:entered_username>/', views.thank_you, name='thank_you'),
]
