from django.urls import path
from school.views.school_api import university_list

urlpatterns = [
    path('university/', university_list, name='list_university')
]