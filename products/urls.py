"""Product  URL Configuration """
from django.urls import path
from products.views import ProductDetailView, filter_object, FilterDetailView

urlpatterns = [
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product"),
    path("filter_by/<str:filter_name>/", filter_object, name="filter-object"),
    path("filter_class/<str:category_id>/", FilterDetailView.as_view(), name="filter-object"),
]
