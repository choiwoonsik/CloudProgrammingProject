from django.views import View
from django.views.generic import FormView, DetailView, UpdateView
from django.shortcuts import render, redirect,reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from users.forms import SignUpForm
from users.models import User
from . import models, forms

def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


class LoginView(FormView):

  template_name = "users/login.html"
  form_class = forms.LoginForm

  def form_valid(self, form):
    email = form.cleaned_data.get("email")
    password = form.cleaned_data.get("password")
    user = authenticate(self.request, username=email, password=password)
    if user is not None:
        login(self.request, user)
        # return redirect(reverse("core:home"))
    return super().form_valid(form)
  
  def get_success_url(self):
    next_arg = self.request.GET.get("next")
    if next_arg is not None:
        return next_arg
    else:
        return reverse("core:home")


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class ProfileView(DetailView):

  template_name = "users/user_profile.html"
  model = models.User
  context_object_name = "user_obj"

class ProfileUpdateView(UpdateView):

  template_name = "users/user_update.html"
  model = User
  fields = ("first_name", "last_name", "bio", "preference", "language", "fav_book_cat", "fav_movie_cat",)

  def get_success_url(self):
    return reverse("users:profile", kwargs={"pk":self.request.user.pk})

  def get_form(self, form_class=None):
    form = super().get_form(form_class=form_class)
    form.fields['first_name'].widget.attrs = {"placeholder": "First Name"}
    form.fields['last_name'].widget.attrs = {"placeholder": "Last Name"}
    form.fields['bio'].widget.attrs = {"placeholder": "bio"}
    form.fields['language'].widget.attrs = {"placeholder": "Language"}
    form.fields['fav_book_cat'].widget.attrs = {"placeholder": "Favorit Book Cat"}
    form.fields['fav_movie_cat'].widget.attrs = {"placeholder": "Favorit Movie Cat"}
    return form

class UserPasswordChangeView(PasswordChangeView):

  template_name = "users/user_password.html"

  def get_success_url(self):
    return reverse("users:update", kwargs={"pk":self.request.user.pk})

  def get_form(self, form_class=None):
    form = super().get_form(form_class=form_class)
    form.fields['old_password'].widget.attrs = {"placeholder": "Before password"}
    form.fields['new_password1'].widget.attrs = {"placeholder": "Change password"}
    form.fields['new_password2'].widget.attrs = {"placeholder": "Confirm password"}
    return form