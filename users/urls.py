from django.urls import path
from .views import (
    UserCreateAPIView,
    ObtainAuthToken,
)

urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='user_create'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
]