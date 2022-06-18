from django.shortcuts import render
from movies.models import Movie
from books.models import Book


def resolve_home(request):
    movies = Movie.objects.all().order_by('-pk')[:4]
    books = Book.objects.all().order_by('-pk')[:4]

    return render(request, "home.html", {
        "movies": movies,
        "books": books,
        "page_title": "Home"
    })
