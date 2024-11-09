from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from school.models import University
from school.serializers import UniversitySerializer