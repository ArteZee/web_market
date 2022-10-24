"""Cart  URL Configuration """
from django.urls import path
from cart.views import cart_add,cart_detail,cart_remove


app_name = "cart"
urlpatterns = [
    path("cart/",cart_detail,name="cart_detail"),
    path("cart_add/<str:slug>",cart_add,name="cart_add"),
    path("cart_remove/<str:slug>",cart_remove,name= "cart_remove"),

]
