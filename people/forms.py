from django import forms
from . import models

class CreatePersonForm(forms.ModelForm):
  class Meta:
      model = models.Person
      fields = (
        "name",
        "photo",
        "kind",
      )

  def save(self, *args, **kwargs):
    person = super().save(commit=False)
    return person
