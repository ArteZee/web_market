from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from products.models import ProductModel


class HomepageListView(ListView):
    queryset = ProductModel.objects.all()
    template_name = "homepage.html"


class CartTemplateView(TemplateView):
    template_name = "cart.html"


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
