from django.contrib import admin
from books.models import Book

admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "rating",
    )

    list_filter = (
        "year",
        "rating",
        "category"
    )
