from rest_framework import permissions, status, authentication, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Cart, CartProduct
from products.models import Product
from .serializers import AddToCartSerializer, CartSerializer

class CartDetailsAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        '''
        Get cart of logged in user
        '''
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddToCartAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''
        Add a product to cart
        '''
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get('product_id')
            quantity = serializer.validated_data.get('quantity')

            cart, created = Cart.objects.get_or_create(user=request.user)
            product = get_object_or_404(Product, id=product_id)

            cart_item, created = CartProduct.objects.get_or_create(cart=cart, quantity=quantity, product=product)
            cart_item.save()

            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RemoveFromCartAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        '''
        Remove a product from cart
        '''
        product_id = request.data.get('product_id')

        if product_id is None:
            return Response({'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart = Cart.objects.get(user=request.user)

        if not cart.products.filter(id=product_id).exists():
            return Response({'message': 'Product not in cart'}, status=status.HTTP_400_BAD_REQUEST)

        cart.products.remove(product)
        cart.save()

        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)