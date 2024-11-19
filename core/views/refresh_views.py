from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({"erreur": "Refresh token manquant"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)

            response = Response({"message": "Token rafraichi avec sucess"}, status=status.HTTP_200_OK)
            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="Strict",
            )
            return response
        except Exception as e:
            return Response({"erreur": "Token de rafraichissement incorrect"}, status=status.HTTP_400_BAD_REQUEST)
