from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView


# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"

    def form_valid(self, form):
        form.save()
        return redirect("thank_you", entered_username=form.cleaned_data["username"])

    def form_invalid(self, form):
        return self.render_to_response({"form": form})


# def review(request):
#     """
#     Render the review page.
#     """
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # Process the form data

#             form.save()

#             # review = Review(
#             #     username=form.cleaned_data["username"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"],
#             # )
#             # review.save()
#             entered_username = form.cleaned_data["username"]
#             # Here you can save the data to the database or perform other actions
#             # Redirect to thank you page with the entered username
#             return redirect("thank_you", entered_username=entered_username)

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {"form": form})


# def thank_you(request, entered_username):
#     """
#     Render the thank you page.
#     """
#     # This view can be used to display a thank you message after form submission
#     return render(request, "reviews/thank_you.html", {"username": entered_username})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs["entered_username"]
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"
