from django.urls import reverse
from django.db import models
from core.models import CoreModel


class Movie(CoreModel):
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(upload_to='movie/images/%Y/%m/%d/', null=True, blank=True)
    rating = models.FloatField()
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, related_name="movies")
    director = models.CharField(max_length=30)
    cast = models.CharField(max_length=30)
    author = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movie", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created_at"]
