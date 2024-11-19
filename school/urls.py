from django.urls import path
from school.views.school_api import universities_home_list

urlpatterns = [
    path('universities/home_list', universities_home_list, name='home_list_universities')
]