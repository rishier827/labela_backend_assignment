from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'description', 'image', 'is_active']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        return value

    def validate_price(self, value):
        if value is None or value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate_category(self, value):
        if not value:
            raise serializers.ValidationError("Category is required.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description is required.")
        return value

    def validate_is_active(self, value):
        if value is None:
            raise serializers.ValidationError("Is_active field is required.")
        return value
    
class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'description', 'image', 'is_active']

    def validate_name(self, value):
        if value is not None and not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_price(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate_category(self, value):
        if value is not None and not value:
            raise serializers.ValidationError("Category cannot be empty.")
        return value

    def validate_description(self, value):
        if value is not None and not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def validate_is_active(self, value):
        if value is not None and not isinstance(value, bool):
            raise serializers.ValidationError("Is_active field must be a boolean.")
        return value