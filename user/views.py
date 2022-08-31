from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView
from user.forms import RegisterForm, LoginForm
from user.models import UserModel


class UserLoginView(LoginView):
    model = UserModel
    form_class = LoginForm
    template_name = "login.html"


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


class UserView(DetailView):
    model = UserModel
    template_name = "user_profile.html"

    def get_object(self, **kwargs):
        return UserModel.objects.get(username=self.kwargs['slug'])


class UserCreateView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = "register.html"
    success_url = "/"


class UserUpdateView(UpdateView):
    model = UserModel
    form_class = RegisterForm
    template_name = "register.html"

    def get_object(self, **kwargs):
        return UserModel.objects.get(username=self.kwargs['slug'])
