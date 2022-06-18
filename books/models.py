from django.urls import reverse
from django.db import models
from core.models import CoreModel


class Book(CoreModel):
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.FloatField()
    writer = models.CharField(max_length=30)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created_at"]
