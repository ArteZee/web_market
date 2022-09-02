from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from cart.forms import CartAddProductForm
from .models import ProductModel


# def product(request: HttpRequest, product_slug) -> HttpResponse:
#     try:
#         context = {"object": ProductModel.objects.get(product_slug=product_slug)}
#         return render(request, "product.html", context)
#     except ProductModel.DoesNotExist:
#         raise Http404 ("Page not Found")

class ProductDetailView(DetailView):
    model = ProductModel
    template_name = "product.html"

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context["object_list"]=cart_product_form
        return context


    def get_object(self, **kwargs):

        return ProductModel.objects.get(slug=self.kwargs['slug'])

    # def product_detail(request, id, slug):
    #     product = get_object_or_404(ProductModel,
    #                                 id=id,
    #
    #                                 available=True)
    #     cart_product_form = CartAddProductForm()
    #     return render(request, 'product.html', {'product': product,
    #                                                         'cart_product_form': cart_product_form})


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
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] =ProductModel.objects.filter(category_id=self.kwargs['category_id'])
        return context