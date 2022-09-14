from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView, CreateView
from cart.forms import CartAddProductForm
from .models import ProductModel
from products.forms import ProductForm
from .utils import ObjectCreateMixin


class ProductCreate(ObjectCreateMixin, View):
    form_model = ProductForm
    template = "create_update_form.html"


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context["object_list"] = cart_product_form
        return context

    def get_object(self, **kwargs):
        return ProductModel.objects.get(slug=self.kwargs['slug'])


def filter_object(request: HttpRequest, filter_name) -> HttpResponse:
    if filter_name == "available":
        element_product = ProductModel.objects.filter(available=True)
    elif filter_name == "50k":
        element_product = ProductModel.objects.filter(price__lt=50000)
    elif filter_name == "50k-99k":
        element_product = ProductModel.objects.filter(price__range=(50_000, 99_000))
    elif filter_name == "99k-200k":
        element_product = ProductModel.objects.filter(price__range=(99_000, 200_000))
    elif filter_name == "200k-":
        element_product = ProductModel.objects.filter(price__gte=200_000)
    context = {"object_list": element_product}
    return render(request, "homepage.html", context)


class FilterDetailView(ListView):
    model = ProductModel
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = ProductModel.objects.filter(category_id=self.kwargs['category_id'])
        return context
