from django.db import models
import os


# Create your models here.
def upload_form(instace, filename):
    return os.path.join('uploads/photo/', filename)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    category_image = models.ImageField(upload_to='images/', blank=True)


def __str__(self):
    return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='p_category', null=True, blank=True)
    name_tr = models.CharField(max_length=250, null=True, blank=True)
    name_en = models.CharField(max_length=250, null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name='Durumu')
    price = models.DecimalField(blank=True, null=True, verbose_name='Fiyat',
                                max_digits=7,
                                decimal_places=2)
    photo = models.FileField(upload_to=upload_form)

    def __str__(self):
        return self.name_tr
