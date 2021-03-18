import itertools

import django_tables2 as tables
from .models import *


class ProductTable(tables.Table):
    counter = tables.Column(verbose_name='#', empty_values=(), orderable=False)
    edit = tables.TemplateColumn(
        template_name='farmer_app/base/table_buttons.html',
        extra_context={"item_type": "product"})

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
