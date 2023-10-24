from django.urls import path
from .views import SignUpView, SessionKeyExample

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("session/", SessionKeyExample.as_view())
]