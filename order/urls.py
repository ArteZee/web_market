from django.urls import path
from order.views import order_create,history
from .api_views import OrderViewSet
app_name = "order"

urlpatterns = [
    path("order/create/<str:username>/",order_create,name= "order-create"),
    path("order/history/<int:user_id>/",history,name= "order-history"),
    path("api/order/",OrderViewSet.as_view({"get":"list"}),name="api-order"),
    path("api/order/<int:pk>", OrderViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"})),



]