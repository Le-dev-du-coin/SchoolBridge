from student.serializers import RegisterSerializer, LoginSerialiser, OtpSerializer, StudenProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from core.models import User, OnetimePasscode
from rest_framework.response import Response
from core.utils import send_otp_code
from django.http import JsonResponse
from student.models import Student
from rest_framework import status

# Register
@api_view(['POST'])
@permission_classes([AllowAny])
def student_register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        email = serializer.validated_data["email"]

        #Send OTP Code for email verification
        send_otp_code(email=email)

        return Response({
            "user": {
                "full_name": f"{user.first_name} {user.last_name}",
                "email": user.email
            },
            "message": f"Salut {user.last_name} ! Merci pour votre inscription. Consultez votre email pour vérifier votre compte",
            "token": token.key
        }, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Code OTP verification
@api_view(['POST'])
def otp_verification(request):
    serializer = OtpSerializer(data=request.data)
    if serializer.is_valid():
        code = serializer.validated_data["code"]
        try:
            otp_code = OnetimePasscode.objects.get(user=request.user)
        except:
            return Response({"error": "Vous n'avez pas encore recu de code de verification. Envoyer le code"}, status=status.HTTP_400_BAD_REQUEST)
        if  code != otp_code:
            return Response({"error": "Code de verification incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        OnetimePasscode.objects.get(user=request.user).delete()
        return Response({"Success": "Email verifie avec success"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerialiser(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Identifiant ou mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Student's profile
@api_view(['GET'])
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