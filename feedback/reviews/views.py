from django.shortcuts import render, redirect
from .forms import ReviewForm


# Create your views here.


def review(request):
    """
    Render the review page.
    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Process the form data
            entered_username = form.cleaned_data["username"]
            # Here you can save the data to the database or perform other actions
            # Redirect to thank you page with the entered username
            return redirect("thank_you", entered_username=entered_username)

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request, entered_username):
    """
    Render the thank you page.
    """
    # This view can be used to display a thank you message after form submission
    return render(request, "reviews/thank_you.html", {"username": entered_username})
