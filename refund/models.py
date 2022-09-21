from django.db import models

from order.models import OrderModel
from user.models import UserModel


class RefundOrderModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    process = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.id)
