from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from products.models import ProductModel


def homepage(request: HttpRequest) -> HttpResponse:
    element_product = ProductModel.objects.all()
    return render(request, "homepage.html", {"element_product": element_product})


def about(request: HttpRequest) -> HttpResponse:
    """
    fucntion return render html cart
    :param request:
    :return:
    """
    return render(request, "cart.html")
