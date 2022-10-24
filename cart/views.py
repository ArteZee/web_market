from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from cart.cart import Cart
from products.models import ProductModel
from cart.forms import CartAddProductForm

# Create your views here.
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request: HttpRequest, slug) -> HttpResponse:
    cart = Cart(request)
    product = get_object_or_404(ProductModel, slug=slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd["quantity"],
                 update_quantity=cd["update"])
    return redirect("cart:cart_detail")
def cart_remove(request, slug):
    cart= Cart(request)
    product = get_object_or_404(ProductModel, slug=slug)
    cart.remove(product)
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = Cart(request)
    context = {"cart":cart}
    return render(request,"cart/detail.html", context)