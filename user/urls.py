"""User App URL Configuration """
from django.urls import path
from user.views import UserCreateView, UserUpdateView, UserView,UserLoginView,logout_view

app_name = "user"
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("logout/",logout_view, name="logout"),
    path("<slug:slug>", UserView.as_view(), name="user"),
    path("<slug:slug>/update/", UserUpdateView.as_view(), name="change-data")
]
