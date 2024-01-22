from rest_framework import serializers

from products.models import Product
from .models import Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'deliver_at', 'created_at', 'updated_at', 'products']
        read_only_fields = ['id', 'user', 'cart', 'created_at', 'updated_at', 'products']
        extra_kwargs = {
            'deliver_at': {'required': True},
        }

    def get_products(self, obj):
        return ProductSerializer(obj.cart_items.all(), many=True).data