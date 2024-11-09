from rest_framework import serializers
from student.models import Student
from core.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=68)
    passwordw2 = serializers.CharField(write_only=True, min_length=8, max_length=68)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "password2")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            validated_data['password'] == validated_data['password2']

            user = User.objects.create_user(
                first_name = validated_data["first_name"],
                last_name = validated_data["first_name"],
                email = validated_data["email"],
                password = validated_data['password']
            )
            return user
        except:
            pass

class LoginSerialiser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



class StudenProfile(serializers.Serializer):
    pass