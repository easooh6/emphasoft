from accounts.serializers import RegisterSerializer
from rest_framework.serializers import ValidationError
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user():
    data = {
        "username": "test_username",
        "password": "test_password",
        "email": "testemail@test.com",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
    }
    return data


@pytest.mark.django_db
def test_create_user(user):
    assert User.objects.create_user(**user)


@pytest.mark.django_db
def test_register_serializer(user):

    serializer = RegisterSerializer(data=user)
    assert serializer.is_valid(), serializer.errors
    serializer.save()

    assert User.objects.filter(username=user["username"]).exists()


@pytest.mark.django_db
def test_register_invalid_serializer_repeat_email(user):
    serializer = RegisterSerializer(data=user)
    serializer.is_valid()
    serializer.save()

    new_user = user.copy()
    new_user["username"] = "new_test_username"

    with pytest.raises(ValidationError):
        serializer = RegisterSerializer(data=new_user)
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_register_invalid_serializer_repeat_username(user):
    serializer = RegisterSerializer(data=user)
    serializer.is_valid()
    serializer.save()

    new_user = user.copy()
    new_user["email"] = "new_test_email"

    with pytest.raises(ValidationError):
        serializer = RegisterSerializer(data=new_user)
        serializer.is_valid(raise_exception=True)
