from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number, name="monthly-challenge-int"),
    path("<str:month>", views.monthly_challenge, name="monthly-challenge"),
]

