"""Product  URL Configuration """
from django.urls import path, include
from products.views import ProductDetailView, filter_object, FilterDetailView,ProductCreate,ProductUpdate
# from .api_views import ProductViewSet,CategoryViewSet


app_name = "product"
urlpatterns = [
    path("product/create/",ProductCreate.as_view(),name="product-create"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product"),
    path("product/update/<slug:slug>/",ProductUpdate.as_view(),name="product-update"),
    path("filter_by/<str:filter_name>/", filter_object, name="filter-object"),
    path("filter_class/<str:category_id>/", FilterDetailView.as_view(), name="filter-object"),
    path("api/",include("api.urls",namespace="api")),


]
