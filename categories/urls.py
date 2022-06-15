from django.urls import path
from categories.views import resolve_categories
from . import views

app_name="categories"

urlpatterns = [
  path("", resolve_categories, name="categories"),
  path("search/", views.SearchView.as_view(), name="search"),
]
