from django.urls import path
from .views import RegisterAPIView, LogOutAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(),name="register"),
    path('logout/', LogOutAPIView.as_view(),name="logout"),    
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]