from django.db import models
import os


# Create your models here.
def upload_form(filename):
    return os.path.join('uploads/photo/', filename)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    category_image = models.ImageField(upload_to="image", blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='p_category', null=True,
                                 blank=True)
    name_tr = models.CharField(max_length=250, null=True, blank=True,
                               verbose_name='Ürün Adı (TR)')
    name_en = models.CharField(max_length=250, null=True, blank=True,
                               verbose_name='Ürün Adı (EN)')
    status = models.BooleanField(default=False, verbose_name='Durumu')
    price = models.DecimalField(blank=True, null=True, verbose_name='Fiyat',
                                max_digits=7,
                                decimal_places=2)
    photo = models.FileField(upload_to='image', null=True, blank=True,
                             verbose_name='Ürün Görseli')

    def __str__(self):
        return self.name_tr


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL,
                                   null=True)
    quantity = models.IntegerField(verbose_name='Miktar', default=1)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name_tr


class Order(models.Model):
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
