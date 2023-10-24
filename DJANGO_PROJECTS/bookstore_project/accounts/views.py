# accounts/views.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from .mixins import UserRequiredMixin


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"


class ProfileView(UserRequiredMixin, generic.TemplateView):
    template_name = "registration/profile.html"


class UserChangeView(UserRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = "registration/user_change.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChangeView(UserRequiredMixin, PasswordChangeView):
    template_name = "registration/password_change.html"
    success_url = reverse_lazy("password_change_done")
