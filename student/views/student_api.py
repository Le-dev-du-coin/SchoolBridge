from student.serializers import RegisterSerializer, LoginSerialiser
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import aauthenticate
from rest_framework.response import Response
from student.models import Student
from rest_framework import status
from core.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def student_register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": {
                "username": user.username,
                "email": user.email
            },
            "token": token.key
        }, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerialiser(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = aauthenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Identifiant ou mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def student_profile(request, pk):
    user = request.user
    try:
        student = Student.objects.get(user=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)