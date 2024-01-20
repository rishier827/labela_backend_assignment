from django.urls import path
from .views import (
    ProductListApiView,
)

urlpatterns = [
    path('', ProductListApiView.as_view()),
]
