from rest_framework import serializers

from .models import Order, Item
from store.models import Product


class ItemsProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['url', 'title', 'image']


class ItemGETSerializer(serializers.ModelSerializer):
    product = ItemsProductSerializer()

    class Meta:
        model = Item
        fields = ['id', 'product', 'order', 'quantity', 'prize']


class ItemPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'product', 'order', 'quantity', 'prize']


class OrderSerializer(serializers.ModelSerializer):
    items = ItemGETSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'url', 'owner', 'created', 'finished', 'status',
                  'items', 'total_prize']
