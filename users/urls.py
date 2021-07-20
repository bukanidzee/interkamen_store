from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CustomUserViewSet

router = SimpleRouter()

router.register('customuser', CustomUserViewSet, basename='customuser')

urlpatterns = [
    path('', include(router.urls))
]
