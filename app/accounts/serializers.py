from rest_framework.serializers import (
    CharField,
    EmailField,
    ValidationError,
    ModelSerializer,
)
from django.contrib.auth.models import User


class RegisterSerializer(ModelSerializer):

    username = CharField(required=True, min_length=3, max_length=150)
    password = CharField(write_only=True, required=True, min_length=6)
    email = EmailField(required=True)
    first_name = CharField(max_length=150, required=False)
    last_name = CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email is already used")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("Username is already used")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
