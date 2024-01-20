from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductListApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        '''
        List all products
        '''
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        Create a product
        '''
        data = {
            'category': request.data.get('category'),
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'description': request.data.get('description'),
            'image': request.data.get('image'),
            'is_active': request.data.get('is_active')
        }
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    