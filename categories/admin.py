from django.contrib import admin
from categories.models import Category

admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind"
    )

    list_filter = (
        "kind",
    )
