from rest_framework import permissions, status, authentication, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Cart, CartProduct
from products.models import Product
from .serializers import CartSerializer

class CartDetailsAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        '''
        Get cart of logged in user
        '''
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddToCartAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''
        Add a product to cart
        '''
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        if product_id is None or quantity is None:
            return Response({'message': 'Product id and quantity are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartProduct.objects.get_or_create(cart=cart, quantity=quantity, product=product)
        cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RemoveFromCartAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        '''
        Remove a product from cart
        '''
        if (request.data.get('product_id') is None):
            return Response({'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)  
        cart = Cart.objects.get(user=request.user)
        cart.products.remove(request.data.get('product_id'))
        cart.save()
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)