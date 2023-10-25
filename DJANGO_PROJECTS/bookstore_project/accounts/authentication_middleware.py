# accounts/authentication_middleware.py
from django.shortcuts import redirect
from django.urls import reverse


class UserAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path != reverse("accounts:login") and request.path != reverse("accounts:signup"):
                return redirect("accounts:login")
        return self.get_response(request)
