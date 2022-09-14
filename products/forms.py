from django import forms

from products.models import ProductModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
    # def clean_slug(self):
    #     new_slug = self.cleaned_data["slug"].lower()
    #     if new_slug == "create":
    #         raise ValidationError("slug can not be 'create'")
