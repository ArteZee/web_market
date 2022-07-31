"""Product  URL Configuration """
from django.urls import path
from products.views import product_1, product_2, product_3, product_4

urlpatterns = [
    path("wall-e/", product_1, name="product_1"),
    path("r2d2/", product_2, name="product_2"),
    path("c3po/", product_3, name="product_3"),
    path("bender/", product_4, name="product_4"),


]