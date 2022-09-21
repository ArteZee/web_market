from django.contrib import admin

from refund.models import RefundOrderModel


class RefundOrderAdmin(admin.ModelAdmin):
    list_display = "created", "user", "order"
    list_filter = "created", "user"


admin.site.register(RefundOrderModel, RefundOrderAdmin)
