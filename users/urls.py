from django.urls import path

from users.views import logout_view, LoginView, SignUpView, ProfileView, ProfileUpdateView

app_name="users"

urlpatterns = [
  path("logout", logout_view, name="logout"),
  path("login", LoginView.as_view(), name="login"),
  path("signup", SignUpView.as_view(), name="signup"),
  path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
  path("profile/update/<int:pk>/", ProfileUpdateView.as_view(), name="update")
]