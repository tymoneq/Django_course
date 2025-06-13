from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))['rating__avg']

    

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": num_books,
            "average_rating": avg_rating,
        },
    )


def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404("Book not found")

    return render(request, "book_outlet/book_detail.html", {"book": book})
