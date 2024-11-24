from core.serializers import RegisterSerializer, LoginSerialiser, OtpSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate,  login, logout
from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework.authtoken.models import Token
from core.models import User, OnetimePasscode
from rest_framework.response import Response
from core.utils import send_otp_code
from django.http import JsonResponse
from rest_framework import status




# -------------------------- 
# Register
# --------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def auth_register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        
        if User.objects.filter(email=email):
            return Response({"erreur": "Email déjà existant, veuillez choisir un autre email."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        
        #Send OTP Code for email verification
        send_otp_code(email=email)

        return Response({
            "user": {
                "full_name": f"{user.first_name} {user.last_name}",
                "email": user.email
            },
            "message": f"Salut {user.last_name} ! Merci pour votre inscription. Nous avons envoyé un code de verification a l'email: {email}",
        }, status= status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------- 
# Code OTP verification
# --------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def otp_verification(request):
    print(f"Utilisateur authentifié : {request.user.is_authenticated}")
    serializer = OtpSerializer(data=request.data)
    if serializer.is_valid():
        code = serializer.validated_data["code"]
        print(serializer.data)
        try:
            otp_code = OnetimePasscode.objects.get(user=request.user)
        except OnetimePasscode.DoesNotExist:
            return Response({"error": "Vous n'avez pas encore reçu de code de vérification. Envoyez le code."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not otp_code.is_valid():
            otp_code.delete()  # Supprimez le code expiré
            return Response({"error": "Le code de vérification a expiré. Veuillez demander un nouveau code."}, status=status.HTTP_400_BAD_REQUEST)

        if code != otp_code.code: 
            return Response({"error": "Code de vérification incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Mettre à jour l'utilisateur pour le marquer comme validé
        user = request.user
        user.is_validated = True
        user.save()
        
        # Supprimer le code OTP après validation
        otp_code.delete()
        return Response({"success": "Email vérifié avec succès"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------- 
# Login
# --------------------------
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny])
def aut_login(request):
    if request.user.is_authenticated:
        return Response({"message": "Vous êtes déjà connecté."}, status=status.HTTP_200_OK)

    serializer = LoginSerialiser(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(request, email=email, password=password)
        
        if user is not None:

            # Génération des tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "success": "Connexion réussie"
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Identifiant ou mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------- 
# Logout
# --------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def auth_logout(request):
    user = request.user
    logout(request)
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_200_OK)

# -------------------------- 
# Verification de la validation email au cas ou l'utilisateur 
# quitte la page de verification pour une raison ou pour une autre
# --------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_validation(request):
    user = request.user
    return Response({"isValidated": user.is_validated}, status=status.HTTP_200_OK)


# -------------------------- 
# Resend OPT Code
# --------------------------
@api_view(['POST'])
def resend_otp_code(request):
    user = request.user
    email = user.email
    
    otp_code = OnetimePasscode.objects.get(user=user)
    otp_code.delete()
    
    send_otp_code(email=email)
    return Response({"success": "Code renvoyé avec success"}, status.HTTP_200_OK)