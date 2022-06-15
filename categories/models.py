from django.db import models
from core.models import CoreModel


class Category(CoreModel):
    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"

    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=15)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def all_category(self):
        category_list = (
            "Science Fiction",
            "Humor",
            "Action",
            "Animation",
            "Comedy",
            "Crime",
            "Documentary",
            "Drama",
            "Family",
            "Music",
            "Musical",
            "Sci-Fi",
            "Sport",
            "Superhero",
            "War",
            "Adventure",
            "Fantasy",
            "Horror",
            "Mystery",
            "Romance",
            "Thriller",
        )
        return category_list
