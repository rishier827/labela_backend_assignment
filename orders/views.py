from rest_framework.views import APIView
from rest_framework import permissions, status, authentication
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from carts.models import Cart

class OrdersListAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        '''
        Get orders of logged in user
        '''
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        '''
        Create an order
        '''
        if (request.data.get('deliver_at') is None):
            return Response({'message': 'Cart id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        deliver_at = request.data.get('deliver_at')

        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if not cart.products.exists():  # Check if the cart is empty
            return Response({'message': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)
        
        order = Order.objects.create(user=request.user, deliver_at=deliver_at)
        order.cart_items.set(cart.products.all())
        order.save()

        cart.products.clear()
        cart.refresh_from_db()  # Refresh the cart instance

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CancelOrderAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        '''
        Cancel an order
        '''
        if (request.data.get('order_id') is None):
            return Response({'message': 'Order id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            order = Order.objects.get(id=request.data.get('order_id'), user=request.user)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        
        order.delete()
        return Response({'message': 'Order cancelled'}, status=status.HTTP_200_OK)



    