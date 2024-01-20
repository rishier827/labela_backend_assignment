from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  # or serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']  # add other fields as needed