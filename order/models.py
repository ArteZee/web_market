from django.db import models

# Create your models here.
from products.models import ProductModel
from user.models import UserModel


class OrderModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel,on_delete= models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    process = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.id)

    def get_cost(self):
        return self.price * self.quantity



