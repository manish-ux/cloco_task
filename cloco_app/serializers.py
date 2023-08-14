from rest_framework import serializers
from .models import User


class SignUpFormSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[],)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "phone",
            "dob",
            "gender",
            "address",
        ]


class LoginFormSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[],)

    class Meta:
        model = User
        fields = ["username", "password"]
