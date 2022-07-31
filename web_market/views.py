from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def homepage(request: HttpRequest) -> HttpResponse:
    """
    fucntion return render html homepage
    :param request:
    :return:
    """
    return render(request, "homepage.html")


def about(request: HttpRequest) -> HttpResponse:
    """
    fucntion return render html cart
    :param request:
    :return:
    """
    return render(request, "cart.html")
