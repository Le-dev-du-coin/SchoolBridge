from core.serializers import RegisterSerializer, LoginSerialiser, OtpSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from core.models import User, OnetimePasscode
from rest_framework.response import Response
from core.utils import send_otp_code
from django.http import JsonResponse
from rest_framework import status




# Register
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
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
            "message": f"Salut {user.last_name} ! Merci pour votre inscription. Nous avons envoyé un code de verification a l'email: {email}",
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
        except OnetimePasscode.DoesNotExist:
            return Response({"error": "Vous n'avez pas encore recu de code de verification. Envoyer le code"}, status=status.HTTP_400_BAD_REQUEST)
        
        if code != otp_code.code:  # Assurez-vous de comparer avec le bon champ
            return Response({"error": "Code de verification incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Mettre à jour l'utilisateur pour le marquer comme validé
        user = request.user
        user.is_validated = True
        user.save()
        
        # Supprimer le code OTP après validation
        otp_code.delete()
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
            if not user.is_validated:
                # Envoyer l'OTP si l'utilisateur n'est pas validé
                send_otp_code(email=user.email)
                return Response({"error": "Votre compte n'est pas encore validé. Un OTP a été envoyé à votre email."}, status=status.HTTP_403_FORBIDDEN)
            
            token, created = Token.objects.get_or_create(user=user)
            
            # Définir le cookie avec les options sécurisées
            response = JsonResponse({'token': token.key})
            response.set_cookie(
                key='accessToken',
                value=token.key,
                httponly=True,  # Empêche l'accès via JavaScript
                secure=True,    # Envoie le cookie uniquement sur HTTPS
                samesite='Lax'  # Limite l'envoi du cookie dans les requêtes intersites
            )
            return response
        
        return Response({"error": "Identifiant ou mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
