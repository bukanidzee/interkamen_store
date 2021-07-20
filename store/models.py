from django.db import models
from djmoney.models.fields import MoneyField


class Product(models.Model):
    title = models.CharField('Название', max_length=100, blank=True)
    prize = MoneyField('Цена, руб', null=True, default=0, max_digits=7,
                                    decimal_places=2, default_currency='RUB')
    description = models.TextField('Описание продукта')
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['title']
# Create your models here.
