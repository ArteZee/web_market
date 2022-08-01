"""Product  URL Configuration """
from django.urls import path
from products.views import product

urlpatterns = [

    path("product/<str:product_name>/", product, name="product"),


]