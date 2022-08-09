from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import ProductModel


def product(request: HttpRequest, product_name) -> HttpResponse:
    element_product = ProductModel.objects.all()
    for el in element_product:
        if el.product_slug == product_name:
            return render(request, "product.html", {"el": el})
