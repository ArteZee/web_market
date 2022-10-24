from django.contrib import admin

from order.models import OrderModel


class OrderProductAdmin(admin.ModelAdmin):

    list_display = "created", "user", "product","quantity"
    list_filter = "created", "user"
admin.site.register(OrderModel,OrderProductAdmin)

