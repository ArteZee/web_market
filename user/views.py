from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from user.forms import RegisterForm, LoginForm, Edit_LoginForm
from user.models import UserModel


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            redirect_url = reverse("homepage")
            return HttpResponseRedirect(redirect_url)
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))


def user_view(request: HttpRequest, slug) -> HttpResponse:
    try:
        context = {"object": UserModel.objects.get(username=slug)}
        return render(request, "user_profile.html", context)
    except UserModel.DoesNotExist:
        raise Http404


def register_view(request: HttpRequest, ) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

            redirect_url = reverse("user:login")
            return HttpResponseRedirect(redirect_url)

    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def change_data_user(request: HttpRequest, slug) -> HttpResponse:
    try:
        instance = UserModel.objects.get(username=slug)
    except UserModel.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = Edit_LoginForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            redirect_url = form.instance.get_absolute_url()
            return HttpResponseRedirect(redirect_url)

    else:
        form = RegisterForm(instance=instance)
    return render(request, "register.html", {"form": form})
