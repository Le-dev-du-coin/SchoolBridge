from core.models import User, OnetimePasscode
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=68)
    password2 = serializers.CharField(write_only=True, min_length=8, max_length=68)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password", "password2"]
        extra_kwargs = {'password': {'write_only': True}, "password2": {"write_only": True}}
        read_only_field = ["is_active", "is_validated"]

    def validate(self, attrs):
        password = attrs.get("password", "")
        password2 = attrs.get("password2", "")
        if password != password2:
            raise serializers.ValidationError("Mot de passe non identique")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop("password2", None)

        user = User(**validated_data)
        user.set_password(password) # Hash the user's password
        user.save()
        return user

class OtpSerializer(serializers.ModelSerializer):
    code = serializers.CharField(min_length=6, max_length=6)

    class Meta:
        model = OnetimePasscode
        fields = ["code",]


class LoginSerialiser(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]
