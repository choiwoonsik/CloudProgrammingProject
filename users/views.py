from urllib import request

from django.core.checks import messages
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView
from django.shortcuts import render, redirect, reverse
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
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Was not possible to save the user")
            raise form.ValidationError("Already Registered User")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        else:
            raise form.ValidationError("Already Registered User")
        return super().form_valid(form)


class ProfileView(DetailView):
    template_name = "users/user_profile.html"
    model = models.User
    context_object_name = "user_obj"


class ProfileUpdateView(UpdateView):
    template_name = "users/user_update.html"
    model = User
    fields = ("name", "bio", "preference", "language", "fav_book_cat", "fav_movie_cat",)

    def get_success_url(self):
        return reverse("users:profile", kwargs={"pk": self.request.user.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['name'].widget.attrs = {"placeholder": "Name"}
        form.fields['bio'].widget.attrs = {"placeholder": "Bio"}
        form.fields['language'].widget.attrs = {"placeholder": "Language"}
        form.fields['fav_book_cat'].widget.attrs = {"placeholder": "Favorite Book Cat"}
        form.fields['fav_movie_cat'].widget.attrs = {"placeholder": "Favorite Movie Cat"}
        return form
