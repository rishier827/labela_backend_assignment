from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'deliver_at', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'cart', 'created_at', 'updated_at']
        extra_kwargs = {
            'deliver_at': {'required': True},
        }