from django.contrib import admin
from django.urls import path, include
from testing_app.views import home_view, about_view
from practice.views import practice_view
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about_view, name="about"),
    path("practice/", practice_view, name="practice"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),  # Add this line
    path("", home_view, name="home"),
    path("", include("core.urls")),
]
