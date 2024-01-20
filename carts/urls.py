from django.urls import path
from .views import (
    CartDetailsAPIView,
    AddToCartAPIView,
    RemoveFromCartAPIView,
)

urlpatterns = [
    path('', CartDetailsAPIView.as_view(), name='cart_detail'),
    path('add/', AddToCartAPIView.as_view(), name='cart_add'),
    path('remove/', RemoveFromCartAPIView.as_view(), name='cart_remove'),
]