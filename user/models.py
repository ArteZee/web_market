"""
User application model

"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class UserModel(AbstractUser):
    genders = (
        ("m", "Men"),
        ("f", "Women")

    )
    sex = models.CharField(max_length=1, choices=genders, default="")
    age = models.IntegerField(null=True, blank=True, )

    class Meta:
        db_table = "auth_user"
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_absolute_url(self):
        return reverse("user:user", kwargs={"slug": self.username})
