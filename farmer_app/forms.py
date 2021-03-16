from django import forms
from .models import Category


class ListForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "status", "category_image"]
