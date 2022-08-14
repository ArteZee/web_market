from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import ProductModel


def product(request: HttpRequest, product_name) -> HttpResponse:
    context = {"object": ProductModel.objects.get(product_slug=product_name)}
    return render(request, "product.html", context)


def filter_object(request: HttpRequest, filter_name) -> HttpResponse:
    if filter_name == "available":
        element_product = ProductModel.objects.filter(product_available=True)
    elif filter_name == "50k":
        element_product = ProductModel.objects.filter(product_price__lt=50000)
    elif filter_name == "50k-99k":
        element_product = ProductModel.objects.filter(product_price__range=(50_000, 99_000))
    elif filter_name == "99k-200k":
        element_product = ProductModel.objects.filter(product_price__range=(99_000, 200_000))
    elif filter_name == "200k-":
        element_product = ProductModel.objects.filter(product_price__gte=200_000)
    context = {"element_product": element_product}
    return render(request, "homepage.html", context)


def filter_class(request: HttpRequest, slug) -> HttpResponse:
    context = {"element_product": ProductModel.objects.filter(category_id=slug)}
    return render(request, "homepage.html", context)
