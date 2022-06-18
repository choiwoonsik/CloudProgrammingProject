from django.views.generic import ListView, DetailView, UpdateView, FormView
from django.shortcuts import redirect, reverse
from books.models import Book
from . import forms


class BooksView(ListView):
    model = Book
    paginate_by = 8
    paginate_orphans = 4
    ordering = "-created_at"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Books"
        return context


class BookDetail(DetailView):
    model = Book
    context_object_name = 'book'


class CreateBook(FormView):
    form_class = forms.CreateBookForm
    template_name = "books/book_create.html"

    def form_valid(self, form):
        book = form.save()
        book.save()
        return redirect(reverse("books:book", kwargs={'pk': book.pk}))


class EditBook(UpdateView):
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
