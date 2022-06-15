from django.shortcuts import render
from django.views.generic import View
from . import models


def resolve_categories(request):
  return render(request, "genres.html")

class SearchView(View):

  model = models.Category
  template_name = 'search.html'

  def get(self, request):
    
    category = request.GET.get("category")

    return render(request, "search.html")

    if category:
      pass
    
    else:
      pass
      