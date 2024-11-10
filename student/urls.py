from django.urls import path
from student.views.student_api import student_register, login, otp_verification, student_profile_detail
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)

urlpatterns = [
    path('register/', student_register, name='register'),
    path('otp-validation/', otp_verification, name='otp_verification'),
    path('login/', login, name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('student-profile/<int:pk>/', student_profile_detail, name='student_profile')
]