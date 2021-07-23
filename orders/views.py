from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAdminUser

from .models import Order, Item
from .serializers import OrderSerializer, ItemPOSTSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser, ]


class ItemViewSet(UpdateModelMixin,
                  CreateModelMixin,
                  DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemPOSTSerializer
    permission_classes = [IsAdminUser, ]
