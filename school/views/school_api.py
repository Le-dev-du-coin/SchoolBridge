from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from school.serializers import UniversitySerlializers
from rest_framework.response import Response
from rest_framework import serializers
from school.models import University


# -----------------------------------------------------------------
# Recuperer 10 universtés pour les afficher sur la page d'accueil
# -----------------------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def universities_home_list(request):
    university = University.objects.all()[:10]
    serializer = UniversitySerlializers(university, many=True)
    return Response(serializer.data)