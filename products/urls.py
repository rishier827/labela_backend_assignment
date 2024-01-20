from django.urls import path
from .views import (
    ProductListApiView,
    ProductDetailsApiView,
)

urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('<int:product_id>/', ProductDetailsApiView.as_view()),
]
