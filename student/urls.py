from django.urls import path
from student.views.student_api import student_register, login
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)

urlpatterns = [
    path('register/', student_register, name='register'),
    path('login/', login, name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('profile/', StudentDetailView.as_view(), name='student_profile')
]