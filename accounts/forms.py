from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation Form"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
        )


class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""

    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            "username",
            "email",
        )

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#     class Meta:
#         model = CustomUser
#         fields = ('name', 'email')
