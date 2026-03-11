import pytest
from rooms.models import Room
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_room_creation():
    room = Room.objects.create(name="Conference", price=500, capacity=10)
    assert room.name == "Conference"
    assert room.price == 500
    assert room.capacity == 10


@pytest.mark.django_db
def test_room_creation_invalid_price():
    room = Room(name="Conference_1", price=-1, capacity=10)
    with pytest.raises(ValidationError):
        room.full_clean()


@pytest.mark.django_db
def test_room_creation_invalid_capacity():
    room = Room(name="Conference_2", price=500, capacity=-1)
    with pytest.raises(ValidationError):
        room.full_clean()
