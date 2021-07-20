from django.urls import path, include
from rest_framework.routers import SimpleRouter
# from rest_framework.urlpatterns import format_suffix_patterns

from store import views


router = SimpleRouter()

router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    # path('products/<pk>/image', views.ProductImageShow.as_view(), name='show-image'),
    path('', views.api_root, name='root')
]

# urlpatterns = format_suffix_patterns(urlpatterns)


# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
#
# from store import views
#
#
# urlpatterns = [
#     path('products/', views.ProductList.as_view(), name='product-list'),
#     path('products/<pk>/', views.ProductDetail.as_view(), name='product-detail'),
#     path('products/<int:pk>/image', views.ProductImageShow.as_view(), name='show-image'),
#     path('', views.api_root, name='root')
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
