from rest_framework import serializers
from student.models import Student
from core.models import User, OnetimePasscode




class StudenProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date_of_birth = serializers.DateField()
    country_origin = serializers.CharField(max_length="60")
    phone_number = serializers.CharField(max_length=8)
    education_level = serializers.CharField(max_length=60)
    bac_serie = serializers.CharField(max_length=60)

    class Meta:
        model = Student
        #fields = ('user', 'date_of_birth', 'country_origin', 'phone_number', 'education_level', 'bac_serie')