from django.contrib.auth.models import AbstractUser
from django.db import models
from mainapp.models import Product


# Create your models here.


class User(AbstractUser):
    basket = models.ManyToManyField(Product, related_name='Корзина')
