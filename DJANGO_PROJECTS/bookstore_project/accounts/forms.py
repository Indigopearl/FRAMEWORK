# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model  # Add this import


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = (
            get_user_model()
        )
        fields = ("first_name", "last_name", "email")
