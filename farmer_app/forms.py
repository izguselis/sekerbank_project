from django import forms
from .models import *
from translated_fields.utils import language_code_formfield_callback


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


class BookForm(forms.ModelForm):
    class Meta:
        model = BookTranslation
        fields = [
            "parent",
            "title",
            "description",
        ]


class QuestionForm(forms.ModelForm):
    formfield_callback = language_code_formfield_callback

    class Meta:
        model = Question
        fields = [
            *Question.question.fields,
            *Question.answer.fields
        ]
