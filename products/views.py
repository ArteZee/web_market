from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import ProductModel


def product(request: HttpRequest, product_name) -> HttpResponse:
    context = {"object": ProductModel.objects.get(product_slug=product_name)}
    return render(request, "product.html", context)
