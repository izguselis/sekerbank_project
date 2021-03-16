from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    category_image = models.ImageField(upload_to='images/', blank=True)


def __str__(self):
    return self.category_name
