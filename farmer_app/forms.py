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
            "parent",
            "category_name",
            "status",
            "category_image"
        ]


class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Kullanıcı adı'}
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Email'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Şifre'}
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "is_admin"
        ]

        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                self.fields[field_name].widget.attrs[
                    'placeholder'] = field.label
