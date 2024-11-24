from school.views.school_api import (
    universities_home_list, 
    get_university_by_id, 
    get_universities_by_countries)
from django.urls import path

urlpatterns = [
    path("universities/home_list", universities_home_list, name="home_list_universities"),
    path("universities/<int:pk>/", get_university_by_id, name='get_university_by_id'),
    #path("universities/all", get_university_by_id, name='get_university_all'),
    path("universities/by-countries/", get_universities_by_countries, name='get_university_by_countries'),
]