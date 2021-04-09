from django.db import models
import os
from django.contrib.auth.models import User
from multilingual_model.models import MultilingualModel, \
    MultilingualTranslation
from translated_fields import TranslatedField
from django.utils.translation import gettext_lazy as _

RECEIVED = 0
SHIPPED = 1
DONE = 2
STATUS_CHOICES = (
    (RECEIVED, 'Siparişiniz alındı'),
    (SHIPPED, 'Siparişiniz kargolandı'),
    (DONE, 'Siparişiniz tamamlandı'),
)


# Create your models here.
def upload_form(instance, filename):
    return os.path.join('image/', filename)


class Question(models.Model):
    question = TranslatedField(
        models.CharField(_("soru"), max_length=200),
    )
    answer = TranslatedField(
        models.CharField(_("cevap"), max_length=200),
    )

    def __str__(self):
        return self.question


class BookTranslation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey('Book', related_name='translations',
                               on_delete=models.CASCADE)

    title = models.CharField(max_length=32)
    description = models.TextField()


class Book(MultilingualModel):
    ISBN = models.IntegerField()

    def __unicode__(self):
        return self.unicode_wrapper('title', default='Unnamed')


class Category(models.Model):
    category_name = models.CharField(verbose_name='Kategori Adı',
                                     max_length=100)
    status = models.BooleanField(verbose_name='Durumu',
                                 default=False)
    category_image = models.ImageField(verbose_name='Kategori Görseli',
                                       upload_to=upload_form,
                                       blank=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='parent_cat',
                               null=True,
                               blank=True,
                               verbose_name='Üst Kategorisi')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='p_category',
                                 null=True,
                                 blank=True)
    product_name = models.CharField(max_length=250,
                                    null=True,
                                    blank=True,
                                    verbose_name='Ürün Adı')
    status = models.BooleanField(default=False,
                                 verbose_name='Durumu')
    price = models.DecimalField(blank=True,
                                null=True,
                                verbose_name='Fiyat',
                                max_digits=7,
                                decimal_places=2)
    photo = models.FileField(upload_to=upload_form,
                             null=True,
                             blank=True,
                             max_length=1000,
                             verbose_name='Ürün Görseli')

    def __str__(self):
        return self.product_name


class OrderItem(models.Model):
    product = models.OneToOneField(Product,
                                   on_delete=models.SET_NULL,
                                   null=True)
    quantity = models.IntegerField(verbose_name='Miktar',
                                   default=1)
    is_ordered = models.BooleanField(default=False)

    # date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.product_name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    order_status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                                    default=RECEIVED)

    def get_cart_items(self):
        return sum([item.quantity for item in self.items.all()])

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
