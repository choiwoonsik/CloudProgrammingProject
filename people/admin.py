from django.contrib import admin
from people.models import Person

admin.site.register(Person)


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind"
    )
    list_filter = ("kind",)
