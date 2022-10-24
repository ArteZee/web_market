from django.contrib import admin
from products.models import ProductModel, CategoryModel
from user.models import UserModel

# Register your models here.


class ProductModelAdmin(admin.ModelAdmin):
    """we use objects in ProductModel"""
    list_display = "slug", "price", "available", "count"
    list_display_links = "slug",
    list_editable = "price", "available", "count"
    list_filter = "price", "available", "category"


admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(CategoryModel)
admin.site.register(UserModel)
