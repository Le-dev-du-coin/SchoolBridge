from rest_framework.decorators import api_view, permission_classes
from student.serializers import StudenProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from student.models import Student
from rest_framework import status



# Student's profile
@api_view(['GET', 'PUT'])
@permission_classes([AllowAny])
def student_profile_detail(request, pk):
    user = request.user
    try:
        student = Student.objects.get(pk=user)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.methode == "GET":
        serializer = StudenProfileSerializer(student)
        return JsonResponse(serializer.data)
    return Response(data=StudenProfileSerializer, status=status.HTTP_200_OK)