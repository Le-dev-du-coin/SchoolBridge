from core.views.views import (
    check_authentication,
    otp_verification, 
    check_validation,
    resend_otp_code, 
    auth_register, 
    aut_login,
    auth_logout)
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('auth/register/', auth_register, name='register'),
    path('auth/verify-email/', otp_verification, name='otp_verification'),
    path('auth/token/verify', TokenVerifyView.as_view(), name="token_verify"),
    #path('auth/check-validation/', check_validation, name='check_verification'),
    #path('auth/check-authentication/', check_authentication, name='check_authentication'),
    path('auth/resend-otp/', resend_otp_code, name='resend_otp'),
    path('auth/login/', aut_login, name='login'),
    path('auth/logout/', auth_logout, name='login'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]