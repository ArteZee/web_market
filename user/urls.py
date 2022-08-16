"""User App URL Configuration """
from django.urls import path
from user.views import user_profile, login_view, logout_view, register_view

urlpatterns = [
    path("profile/", user_profile, name="user_profile"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]
