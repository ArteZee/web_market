"""User App URL Configuration """
from django.urls import path
from user.views import login_view, logout_view, register_view, change_data_user, user_view

app_name = "user"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("<slug:slug>", user_view, name="user"),
    path("<slug:slug>/update/", change_data_user, name="change-data")
]
