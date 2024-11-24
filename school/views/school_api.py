from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from school.serializers import UniversitySerlializers
from rest_framework.response import Response
from rest_framework import serializers
from school.models import University
from django.db.models import Q



# -----------------------------------------------------------------
# Recuperer 10 universtés pour les afficher sur la page d'accueil
# -----------------------------------------------------------------
@api_view(['GET',])
@permission_classes([AllowAny])
def universities_home_list(request):
    university = University.objects.filter(country_name="France")[:9]
    serializer = UniversitySerlializers(university, many=True)
    return Response(serializer.data)


# ----------------------------------------------------------------------
# Recuperer les universites base sur les pays favoris de l'utilisateur
# ----------------------------------------------------------------------
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def get_universities_by_countries(request):
    countries = request.GET.get("countries")
    print(countries)
    if countries:
        country_list = countries.split(",")
        print(country_list)
        query = Q()
        for country in country_list:
            query |= Q(country_name__icontains=country)

        universities = University.objects.filter(query)
        if universities:
            print("Success")
        else:
            print("RAS")
    else:
        universities = University.objects.none()
    serializer = UniversitySerlializers(universities, many=True)
    return Response(serializer.data)


# -----------------------------------------------------------------
# Recuperer les details d'une université
# -----------------------------------------------------------------
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def get_university_by_id(request, pk):
    university = University.objects.get(id=pk)
    serializer = UniversitySerlializers(university)
    return Response(serializer.data)
