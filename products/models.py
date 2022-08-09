from django.db import models


class CategoryModel(models.Model):
    name_category = models.CharField(max_length=30)
    slug_category = models.SlugField(unique=True, max_length=30)
    description_category = models.TextField()

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = "slug_category",
        db_table = "products_categorymodel"


class ProductModel(models.Model):
    product_name = models.CharField(max_length=20, blank=True)
    product_slug = models.SlugField(unique=True, max_length=20, blank=True)
    product_price = models.PositiveIntegerField(blank=True)
    product_description = models.TextField(blank=True)
    product_count = models.PositiveIntegerField(blank=True)
    product_available = models.BooleanField(blank=True)
    product_img = models.URLField(blank=True)
    category = models.ForeignKey("CategoryModel", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = "product_slug",
        db_table = "product_base"
