from django.shortcuts import render, redirect
from django.http import Http404


# Create your views here.
challenges = {
    "january": "Eat no meat for the entire month of January.",
    "february": "Walk at least 10,000 steps every day in February.",
    "march": "Complete a 30-day yoga challenge in March.",
    "april": "Read at least one book every week in April.",
    "may": "Plant a tree or a garden in May.",
    "june": "Run a total of 100 miles in June.",
    "july": "Drink at least 2 liters of water every day in July.",
    "august": "Practice meditation for at least 10 minutes every day in August.",
    "september": "Learn a new skill or hobby in September.",
    "october": "Write a daily journal entry for the month of October.",
    "november": "Volunteer for a local charity or community service in November.",
    "december": None,
}


def index(request):
    """
    Render the index page with a welcome message and a list of challenges.
    """
    months = list(challenges.keys())

    return render(request, "challanges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    """
    Render the monthly challenge page based on the month number provided.
    """
    months = list(challenges.keys())

    if month < 1 or month > len(months):
        raise Http404()

    challenge_month = months[month - 1]
    # Redirect to the monthly challenge view with the month name

    return redirect(monthly_challenge, challenge_month)


def monthly_challenge(request, month):
    """
    Render the monthly challenge page based on the month provided.
    """

    try:
        challenge_text = challenges[month.lower()]
        return render(
            request,
            "challanges/challenge.html",
            {"month": month, "challenge_text": challenge_text},
        )
    except:
        raise Http404()
