from student.views.student_api import get_student_preferences, student_profile_detail
from django.urls import path


urlpatterns = [
    path('user/student/preferences/', get_student_preferences, name='get_student_preferences'),
    path('user/student/profile/', student_profile_detail, name='get_student_profile'),
]