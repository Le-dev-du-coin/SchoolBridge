from student.serializers import StudenProfileSerializer, StudenPrefrencesSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from student.models import Student
from rest_framework import status
from core.models import User



# ----------------------------------------
# Preferences de l'etudiant
# ----------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student_preferences(request):
    user = request.user
    try:
        student = Student.objects.get(user=user)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudenPrefrencesSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ----------------------------------------
# Profil de l'etudiant
# ----------------------------------------
@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def student_profile_detail(request):
    user = request.user
    try:
        student = Student.objects.get(user=user)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudenProfileSerializer(student)
        return Response(serializer.data)
        

    if request.method == "PATCH":
        serializer = StudenProfileSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(type(serializer.data['country_origin']))

        user_data = request.data.get('user', {})
        if "firs_name" in user_data:
            student.user.first_name = user_data["first_name"]
        if "last_name" in user_data:
            student.user.last_name = user_data["last_name"]
        if "email" in user_data:
            student.user.email = user_data["email"]
            return Response({"error": "Modification de l'email non autorisée."}, status=status.HTTP_400_BAD_REQUEST)

        student.user.save()

        return Response({"success": "Mise à jour reussi"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)