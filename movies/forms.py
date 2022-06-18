from django import forms
from . import models


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = (
            "title",
            "year",
            "cover_image",
            "rating",
            "category",
            "director",
            "cast",
        )

    def save(self, *args, **kwargs):
        movie = super().save(commit=False)
        return movie
