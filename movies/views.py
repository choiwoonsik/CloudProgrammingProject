from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect, reverse
from movies.models import Movie
from . import forms


class MoviesView(ListView):
    model = Movie
    paginate_by = 4
    ordering = "-created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Movies"
        return context


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'


class CreateMovie(LoginRequiredMixin, CreateView):
    form_class = forms.CreateMovieForm
    template_name = "movies/movie_create.html"

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            movie = form.save()
            movie.save()
            return redirect(reverse("movies:movie", kwargs={'pk': movie.pk}))
        else:
            return redirect('/')


class EditMovie(LoginRequiredMixin, UpdateView):
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.request.user.email == self.get_object().author:
            return super(EditMovie, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
