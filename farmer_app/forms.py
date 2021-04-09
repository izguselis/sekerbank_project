from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "product_name",
            "status",
            "price",
            "photo"
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "parent",
            "category_name",
            "status",
            "category_image"
        ]
