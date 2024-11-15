from core.views import register, otp_verification, login
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)

urlpatterns = [
    path('auth/register/', register, name='register'),
    path('auth/verify-email/', otp_verification, name='otp_verification'),
    path('auth/login/', login, name='login'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]