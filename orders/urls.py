from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import OrderViewSet, ItemViewSet

router = SimpleRouter()

router.register('order', OrderViewSet, basename='order')
router.register('item', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls))
]
