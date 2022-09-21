from django.urls import path
from refund.views import refund_order, all_orders_refund, accept_refund, decline_refund

app_name = "refund"

urlpatterns = [
    path("refund/<str:order_id>/", refund_order, name="refund-order"),
    path("all_refunds/", all_orders_refund, name="all-orders"),
    path("accept_refund/<str:order_id>/", accept_refund, name="accept-refund"),
    path("decline_refun/<str:order_id>/", decline_refund, name="decline-refund"),

]
