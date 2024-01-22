from rest_framework import permissions, status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import Product
from .serializers import ProductSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10 

class ProductListApiView(APIView):

    def get_permissions(self):
        if self.request.method != 'GET':
            self.permission_classes = [permissions.IsAuthenticated,]
        else:
            self.permission_classes = [permissions.AllowAny,]
        return super(ProductListApiView, self).get_permissions()
    
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

    def get(self, request):
        '''
        List all products
        '''
        paginator = CustomPagination()
        products = Product.objects.all()
        context = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class ProductDetailsApiView(APIView):

    def get_permissions(self):
        if self.request.method != 'GET':
            self.permission_classes = [permissions.IsAuthenticated,]
        else:
            self.permission_classes = [permissions.AllowAny,]
        return super(ProductDetailsApiView, self).get_permissions()

    def get_object(self, product_id):
        '''
        Get a product
        '''
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id):
        '''
        Get a product
        '''
        product = self.get_object(product_id)
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, product_id):
        '''
        Update a product
        '''
        product = Product.objects.get(id=product_id)
        data = {
            'category': request.data.get('category'),
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'description': request.data.get('description'),
            'image': request.data.get('image'),
            'is_active': request.data.get('is_active')
        }
        serializer = ProductSerializer(product, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, product_id):
        '''
        Delete a product
        '''
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)