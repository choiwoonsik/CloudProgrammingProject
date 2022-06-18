from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect, reverse
from movies.models import Movie
from . import forms


class MoviesView(ListView):
    model = Movie
    paginate_by = 8
    paginate_orphans = 4
    ordering = "-created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Movies"
        return context


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'


class CreateMovie(CreateView):
    form_class = forms.CreateMovieForm
    template_name = "movies/movie_create.html"

    def form_valid(self, form):
        movie = form.save()
        movie.save()
        return redirect(reverse("movies:movie", kwargs={'pk': movie.pk}))


class EditMovie(UpdateView):
    model = Movie
    template_name = "movies/movie_edit.html"
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )

    def get_object(self, queryset=None):
        movie = super().get_object(queryset=queryset)
        return movie
