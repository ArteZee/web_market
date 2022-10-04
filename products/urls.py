"""Product  URL Configuration """
from django.urls import path
from products.views import ProductDetailView, filter_object, FilterDetailView,ProductCreate,ProductUpdate
from .api_views import ProductViewSet,CategoryViewSet


app_name = "product"
urlpatterns = [
    path("product/create/",ProductCreate.as_view(),name="product-create"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product"),
    path("product/update/<slug:slug>/",ProductUpdate.as_view(),name="product-update"),
    path("filter_by/<str:filter_name>/", filter_object, name="filter-object"),
    path("filter_class/<str:category_id>/", FilterDetailView.as_view(), name="filter-object"),
    path("api/product/",ProductViewSet.as_view({'get': 'list'}),name="api-product"),
    path("api/product/<int:pk>", ProductViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="api-product-detail"),
    path("api/category/",CategoryViewSet.as_view({'get': 'list'}), name="api-category"),
    path("api/category/<int:pk>", CategoryViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="api-category-detail"),



]
