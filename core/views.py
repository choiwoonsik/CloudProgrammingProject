from django.shortcuts import render
from movies.models import Movie
from books.models import Book
from people.models import Person

def resolve_home(request):
  
  movies = Movie.objects.all().order_by('-pk')[:5]
  books = Book.objects.all().order_by('-pk')[:5]
  people = Person.objects.all().order_by('-pk')[:5]
  

  return render(request, "home.html", {
    "movies":movies,
    "books": books,
    "people": people,
    "page_title": "Home"
  })