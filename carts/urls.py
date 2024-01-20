from django.urls import path
from .views import (
    CartDetailsAPIView,
)

urlpatterns = [
    path('', CartDetailsAPIView.as_view(), name='cart_detail'),
]