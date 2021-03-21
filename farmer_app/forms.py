from django import forms

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "name_tr",
            "name_en",
            "status",
            "price",
            "photo"
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "category_name",
            "status",
            "category_image"
        ]
