"""
User application forms
"""

from django.contrib.auth import forms
from user.models import UserModel


class RegisterForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name", "email", "age", "gender", "password1", "password2", ]


class LoginForm(forms.AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ["username", "password"]


class Edit_LoginForm(forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ["username", "password", "first_name", "last_name", "email", "age", "gender", ]
