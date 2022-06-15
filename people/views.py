from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect, reverse
from people.models import Person
from . import forms


class PeopleView(ListView):
  
  model = Person
  paginate_by = 8
  paginate_orphans = 4
  ordering = "-created_at"
  context_object_name = "people"
  template_name = "people/people_list.html"

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All People"
        return context


class PersonDetail(DetailView):
  model = Person
  template_name = "people/person_detail.html"
  context_object_name = 'person'


class CreatePerson(CreateView):
  form_class = forms.CreatePersonForm
  template_name = "people/person_create.html"
  
  def form_valid(self, form):
      person = form.save()
      person.save()
      return redirect(reverse("people:person", kwargs={'pk': person.pk}))

class EditPerson(UpdateView):
  model = Person
  template_name = "people/person_edit.html"
  fields = (
    "name",
    "photo",
    "kind"
  )

  def get_object(self, queryset=None):
    person = super().get_object(queryset=queryset)
    # if book.host.pk != self.request.user.pk:
    #     raise Http404()
    return person