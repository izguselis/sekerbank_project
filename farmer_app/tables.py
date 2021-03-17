import itertools

from django.db.models import Q
import django_tables2 as tables
from .models import *
from django_tables2.utils import A


class ProductTable(tables.Table):
    counter = tables.Column(verbose_name='#', empty_values=(), orderable=False)

    class Meta:
        model = Product
        fields = ('name_tr', 'status', 'price', 'photo')
        sequence = ('name_tr', 'status', 'price', 'photo')

    def render_counter(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter) + 1
