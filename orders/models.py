from django.db import models
from djmoney.models.fields import MoneyField
from djchoices import DjangoChoices, ChoiceItem
from typing import Optional, List, Dict


class Order(models.Model):

    class StatusChoices(DjangoChoices):
        current = ChoiceItem('current', label='текущий')
        processing = ChoiceItem('processing', label='в обработке')
        transporting = ChoiceItem('transporting', label='в доставке')
        closed = ChoiceItem('closed', label='завершенный')
        dropped = ChoiceItem('dropped', label='отмененный')

    owner = models.ForeignKey('users.CustomUser', related_name='orders',
                              on_delete=models.CASCADE, verbose_name='Хозяин')
    created = models.DateTimeField('Создано', auto_now_add=True)
    status = models.CharField('Статус', choices=StatusChoices.choices, max_length=50,
                              default=StatusChoices.current)
    finished = models.DateTimeField('Время завершения', blank=True, null=True)
    total_prize = MoneyField('Цена, руб', null=True, default=0, max_digits=7,
                             decimal_places=2, default_currency='RUB')

    class Meta:
        ordering = ['-created']

    def save(self, *args: List, **kwargs: Dict) -> Optional[None]:
        self.total_prize = sum([item.prize for item in Item.objects.filter(order=self)])
        super().save(*args, **kwargs)

    def find_number_of_order(self):
        return str(list(Order.objects.filter(owner=self.owner).order_by('created')).index(self) + 1)

    def __str__(self):
        return self.owner.username + 's order №' + self.find_number_of_order()


class Item(models.Model):
    product = models.ForeignKey('store.Product', related_name='items',
                                on_delete=models.CASCADE, verbose_name='Продукт')
    order = models.ForeignKey('Order', related_name='items',
                              on_delete=models.CASCADE, verbose_name='Заказ')
    quantity = models.PositiveSmallIntegerField('Количество')
    prize = MoneyField('Цена, руб', null=True, default=0, max_digits=7,
                       decimal_places=2, default_currency='RUB')

    class Meta:
        unique_together = ['order', 'product', ]

    def save(self, *args: List, **kwargs: Dict) -> Optional[None]:
        self.prize = self.product.prize * self.quantity
        super().save(*args, **kwargs)

    def find_number_of_item(self):
        return str(list(Item.objects.filter(order=self.order).order_by('id')).index(self) + 1)

    def __str__(self):
        return self.order.__str__() + 'item №' + self.find_number_of_item()
