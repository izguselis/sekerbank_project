from django.conf import settings
from django.db import models
import os

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
    name_tr = models.CharField(max_length=250,
                               null=True,
                               blank=True,
                               verbose_name='Ürün Adı (TR)')
    name_en = models.CharField(max_length=250,
                               null=True,
                               blank=True,
                               verbose_name='Ürün Adı (EN)')
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
        return self.name_tr


class OrderItem(models.Model):
    product = models.OneToOneField(Product,
                                   on_delete=models.SET_NULL,
                                   null=True)
    quantity = models.IntegerField(verbose_name='Miktar',
                                   default=1)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name_tr


class User(models.Model):
    username = models.CharField(verbose_name="Kullanıcı adı",
                                max_length=50)
    email = models.EmailField(verbose_name="e-mail adresi",
                              max_length=255,
                              unique=True)
    password = models.CharField(verbose_name="Şifre",
                                max_length=50)
    is_admin = models.BooleanField(verbose_name="Admin",
                                   default=False)
    orders = models.ManyToManyField(Product,
                                    blank=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=RECEIVED
                                              )

    def get_cart_items(self):
        return sum([item.quantity for item in self.items.all()])

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
