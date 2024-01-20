from django.urls import path
from .views import (
    OrdersListAPIView,
    CancelOrderAPIView,
)

urlpatterns = [
    path('', OrdersListAPIView.as_view(), name='orders_list'),
    path('cancel/', CancelOrderAPIView.as_view(), name='order_cancel'),
]