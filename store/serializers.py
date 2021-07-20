from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # image = serializers.HyperlinkedIdentityField(view_name='show-image', format='html')

    class Meta:
        model = Product
        fields = ['url', 'id', 'title', 'prize', 'description', 'image']
