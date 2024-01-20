from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart
from .serializers import CartSerializer

class CartDetailsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        '''
        Get cart of logged in user
        '''
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddToCartAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''
        Add a product to cart
        '''
        cart = Cart.objects.get(user=request.user)
        cart.products.add(request.data.get('product_id'))
        cart.save()
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RemoveFromCartAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''
        Remove a product from cart
        '''
        cart = Cart.objects.get(user=request.user)
        cart.products.remove(request.data.get('product_id'))
        cart.save()
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)