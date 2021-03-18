import itertools

import django_tables2 as tables
from .models import *


class ProductTable(tables.Table):
    counter = tables.Column(verbose_name='#', empty_values=(), orderable=False)
    edit = tables.TemplateColumn(
        template_name='farmer_app/base/table_buttons.html',
        extra_context={"item_type": "product", "add_url1": "/add_cart/",
                       "add_url2": "/add_product/",
                       "add_url3": "/delete_product/"})

    class Meta:
        model = Product
        fields = (
            'photo', 'category', 'name_tr', 'status', 'price', 'edit')
        sequence = (
            'counter', 'photo', 'category', 'name_tr', 'status', 'price')
        attrs = {
            "class": "table table-striped table-bordered dt-responsive nowrap",
            "id": "datatable-responsive",
            "cellspacing": "0",
            "width": "100%"
        }

    def render_counter(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter) + 1


class OrderItemTable(tables.Table):
    class Meta:
        model = OrderItem
        fields = (
            'quantity', 'product.name_tr', 'product.price')
        sequence = (
            'quantity', 'product.name_tr', 'product.price')
        attrs = {"class": "table"}


class CategoryTable(tables.Table):
    counter = tables.Column(verbose_name='#', empty_values=(), orderable=False)
    edit = tables.TemplateColumn(
        template_name='farmer_app/base/table_buttons.html',
        extra_context={"item_type": "category",
                       "add_url1": "/add_category/",
                       "add_url2": "/delete_category/"})

    class Meta:
        model = Category
        fields = (
            'category_image', 'category_name', 'status', 'edit')
        sequence = (
            'counter', 'category_image', 'category_name', 'status')
        attrs = {
            "class": "table table-striped table-bordered dt-responsive nowrap",
            "id": "datatable-responsive",
            "cellspacing": "0",
            "width": "100%"
        }

    def render_counter(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter) + 1
