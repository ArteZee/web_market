from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = "slug",
        db_table = "products_categorymodel"


class ProductModel(models.Model):
    name = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(unique=True, max_length=20, blank=True)
    price = models.PositiveIntegerField(blank=True)
    description = models.TextField(blank=True)
    count = models.PositiveIntegerField(blank=True)
    available = models.BooleanField(blank=True)
    img = models.URLField(blank=True)
    category = models.ForeignKey("CategoryModel", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = "slug",
        db_table = "product_base"
