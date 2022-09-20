from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from decimal import Decimal

from cart.cart import Cart
from order.models import OrderModel
from user.models import UserModel


def order_create(request:HttpRequest,username)-> HttpResponse:
    cart = Cart(request)
    user = UserModel.objects.get(username=username)

    for item in cart:
        OrderModel.objects.create(user=user,
                                product=item["product"],
                                  price=item["price"],
                                  quantity=item["quantity"])
        cart.clear()
        return render(request,"order_create.html",{"cart":cart})

def history(request,user_id):
    user_order= OrderModel.objects.filter(user_id=user_id)
    for i in user_order:
        total_price = OrderModel.get_cost(i)
        context = {"object":user_order,"total_price":total_price}
        return render(request,"history_order.html",context)



