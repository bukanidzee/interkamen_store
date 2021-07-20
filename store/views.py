from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Product
from .serializers import ProductSerializer


# class ProductImageShow(generics.GenericAPIView):
#     queryset = Product.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         product = self.get_object()
#         adress = product.image.split('/')[-2:]
#         adress = adress[0] + '/' + adress[1]
#         response = Response('<img src={{media {0}}} height="500">'.format(adress))
#         return response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'продукты': reverse('product-list', request=request, format=format),
        'пользователи': reverse('customuser-list', request=request, format=format),
        'заказы': reverse('order-list', request=request, format=format),
        'части заказов': reverse('item-list', request=request, format=format),
    })


class ProductViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
