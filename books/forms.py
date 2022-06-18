from django import forms
from . import models


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            "title",
            "year",
            "cover_image",
            "rating",
            "category",
            "writer",
        )

    def save(self, *args, **kwargs):
        book = super().save(commit=False)
        return book
