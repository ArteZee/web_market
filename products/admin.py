from django.contrib import admin
from products.models import ProductModel, CategoryModel


# Register your models here.


class ProductModelAdmin(admin.ModelAdmin):
    list_display = "product_slug", "product_price", "product_available", "product_count"
    list_display_links = "product_slug",
    list_editable = "product_price", "product_available", "product_count"
    list_filter = "product_price", "product_available", "category"


admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(CategoryModel)
