from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank-you/<str:entered_username>/', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/favorites/', views.AddFavoriteView.as_view(), name='favorite_review_list'),
    path('reviews/<int:pk>/', views.SingleReviewView.as_view(), name='single_review'),
]
