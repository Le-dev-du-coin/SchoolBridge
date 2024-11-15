from rest_framework.decorators import api_view, permission_classes
from school.serializers import UniversitySerlializers
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from school.models import University

@api_view(['GET'])
@permission_classes([AllowAny])
def university_list(request):
    university = University.objects.all()[:10]
    data = UniversitySerlializers(university)
    return JsonResponse(data, safe=False)