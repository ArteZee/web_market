from django.urls import path
from order.views import order_create,history
app_name = "order"

urlpatterns = [
    path("order/create/<str:username>/",order_create,name= "order-create"),
    path("order/history/<int:user_id>/",history,name= "order-history"),



]