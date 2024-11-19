from rest_framework import serializers
from school.models import University


class UniversitySerlializers(serializers.Serializer):
    class Meta:
        model = University
        fields = ["__all__"]
    