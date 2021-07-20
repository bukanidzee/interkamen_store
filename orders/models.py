from django.db import models
from djmoney.models.fields import MoneyField
from djchoices import DjangoChoices, ChoiceItem


class Order(models.Model):

    class StatusChoices(DjangoChoices):
        current = ChoiceItem('current', label='текущий')
        processing = ChoiceItem('processing', label='в обработке')
        transporting = ChoiceItem('transporting', label='в доставке')
        closed = ChoiceItem('closed', label='завершенный')
        dropped = ChoiceItem('dropped', label='отмененный')


    owner = models.ForeignKey('users.CustomUser', related_name='order',
                                                    on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=StatusChoices.choices, max_length=50,
                                                default=StatusChoices.current)
    finished = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created']


class Item(models.Model):
    product = models.ForeignKey('store.Product', related_name='product',
                                                on_delete=models.CASCADE)
    order = models.ForeignKey('Order', related_name='order',
                                                on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    prize = MoneyField('Цена, руб', null=True, default=0, max_digits=7,
                                    decimal_places=2, default_currency='RUB')


    def save(self, *args, **kwargs):
        self.prize = self.product.prize * self.quantity
        super().save(*args, **kwargs)
