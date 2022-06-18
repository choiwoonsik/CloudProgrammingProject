from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView, UpdateView, FormView

from books.models import Book
from . import forms


class BooksView(ListView):
    model = Book
    paginate_by = 4
    ordering = "-created_at"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Books"
        return context


class BookDetail(DetailView):
    model = Book
    context_object_name = 'book'


class CreateBook(LoginRequiredMixin, FormView):
    form_class = forms.CreateBookForm
    template_name = "books/book_create.html"

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            book = form.save()
            book.save()
            return redirect(reverse("books:book", kwargs={'pk': book.pk}))
        else:
            return redirect('/')


class EditBook(LoginRequiredMixin, UpdateView):

    model = Book
    template_name = 'books/book_edit.html'
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "writer",
    )

    def get_object(self, queryset=None):
        book = super().get_object(queryset=queryset)
        return book

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.request.user.email == self.get_object().author:
            return super(EditBook, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
