# accounts/urls.py

from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("user_change/", views.UserChangeView.as_view(), name="user_change"),
]
