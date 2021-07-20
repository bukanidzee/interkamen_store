from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from djmoney.money import Money

from orders.models import Order, Item
from store.models import Product


class SetupClass(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='secret',
            is_superuser=False,
        )

        self.admin_user = get_user_model().objects.create_user(
            username='testuser2',
            password='secret',
            is_superuser=True,
        )

        self.client.login(username='testuser', password='secret')

        self.order = Order.objects.create(
            owner = self.user,
        )

        self.product = Product.objects.create(
            title = 'test title',
            prize = 15,
            description = 'test description'
        )

        self.item = Item.objects.create(
            product = self.product,
            order = self.order,
            quantity = 2,
        )


class OrdersModelsTests(SetupClass):
    def test_order_user_connection(self):
        self.assertEqual(self.order.owner.username, 'testuser')

    def test_items_connection(self):
        self.assertEqual(self.item.product.title, 'test title')
        self.assertEqual(self.item.order.owner.username, 'testuser')

    def test_prize_counting(self):
        self.assertEqual(self.item.prize, Money('30', 'RUB'))

    def test_urls(self):
        response = reverse(self.item.url)
        self.assertEqual(response.status_code, 200)
        response = reverse(self.order.url)
        self.assertEqual(response.status_code, 200)
