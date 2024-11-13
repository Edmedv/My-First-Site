from django.db import models
from django.db.models import PROTECT
from django.forms import CharField


# Create your models here.


class TypeProduct(models.Model):
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True, default='Без названия')
    price = models.IntegerField(default=0)
    photo = models.FileField(upload_to='photos', default=None,
                              blank=True, null=True, verbose_name='Фото')
    type = models.ForeignKey(TypeProduct, on_delete=PROTECT, null=True)