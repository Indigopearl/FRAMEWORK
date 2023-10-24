# accounts/mixins.py
from django.http import HttpResponseRedirect
from django.urls import reverse

class UserRequiredMixin:
    """Mixin to ensure the user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))  # Replace "login" with your actual login URL
        return super().dispatch(request, *args, **kwargs)
