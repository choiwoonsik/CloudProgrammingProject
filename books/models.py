from django.urls import reverse
from django.db import models
from core.models import CoreModel
import urllib.parse


class Book(CoreModel):
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(upload_to='book/images/%Y/%m/%d/', null=True, blank=True)
    rating = models.FloatField()
    writer = models.CharField(max_length=30)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, related_name="books")
    author = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return urllib.parse.unquote(self.cover_image.url)

    def get_absolute_url(self):
        return reverse("books:book", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created_at"]
