"""Product  URL Configuration """
from django.urls import path
from products.views import product, filter_object, filter_class

urlpatterns = [
    path("product/<str:product_name>/", product, name="product"),
    path("filter_by/<str:filter_name>/", filter_object, name="filter-object"),
    path("filter_class/<str:slug>/", filter_class, name="filter-object"),
]
