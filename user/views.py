from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy


def user_profile(request: HttpRequest, ) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, "user_profile.html")
    return HttpResponseRedirect(reverse_lazy("login"))


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]

        if User.objects.filter(username=username):
            context = {"message": "User already exists"}
            return render(request, "login.html", context)

        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            context = {"message": "Password missmatch"}
            return render(request, "register.html", context)

        User.objects.create_user(username=username, password=password1)
        return HttpResponseRedirect(reverse_lazy("login"))
    return render(request, "register.html")


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse_lazy("login"))
        login(request, user)
        return HttpResponseRedirect(reverse_lazy("homepage"))
    return render(request, "login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
