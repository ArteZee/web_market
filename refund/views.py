from django.shortcuts import render

from order.models import OrderModel
from refund.models import RefundOrderModel


def refund_order(request, order_id):
    order = OrderModel.objects.get(id=order_id)
    order_refund = RefundOrderModel.objects.create(user=order.user,
                                                   order=order, )
    total_price = order.quantity * order.price

    context = {"order_refund": order_refund, "total_price": total_price}
    return render(request, "refund_order.html", context)


def all_orders_refund(request):
    all_order = RefundOrderModel.objects.all()
    context = {"all_order": all_order}
    return render(request, "all_refunds_order.html", context)


def accept_refund(request, order_id):
    refund_order = RefundOrderModel.objects.get(id=order_id)

    product = refund_order.order.product
    product.count += int(refund_order.order.quantity)
    product.save()

    user = refund_order.user
    user.balance += (refund_order.order.quantity * refund_order.order.price)
    user.save()

    order = refund_order.order
    order.process = True
    order.save()

    refund_order.delete()

    return render(request, "all_refunds_order.html")


def decline_refund(request, order_id):
    refund_order = RefundOrderModel.objects.get(id=order_id)

    order = refund_order.order
    order.process = False
    order.save()

    refund_order.delete()
    return render(request, "all_refunds_order.html")
