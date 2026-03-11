import pytest
from rooms.serializers import RoomSerializer, RoomBookingCheckSerializer
from rest_framework import serializers
from rooms.models import Room
from datetime import date, timedelta


@pytest.mark.django_db
def test_room_serializer():
    room = Room.objects.create(name="Meeting", price=500, capacity=5)
    serializer = RoomSerializer(room)
    data = serializer.data
    assert data["name"] == "Meeting"
    assert data["price"] == 500
    assert data["capacity"] == 5


@pytest.mark.django_db
def test_room_check_serializer():

    start = "2026-03-11"
    end = "2026-03-16"

    serializer = RoomBookingCheckSerializer(data={"start": start, "end": end})

    assert serializer.is_valid(), serializer.errors

    data = serializer.validated_data

    assert data["start"].isoformat() == start
    assert data["end"].isoformat() == end


@pytest.mark.django_db
def test_room_check_serializer_invalid_old_date():

    invalid_start = "2010-03-11"
    invalid_end = "2012-03-16"

    serializer = RoomBookingCheckSerializer(
        data={"start": invalid_start, "end": invalid_end}
    )

    with pytest.raises(serializers.ValidationError):
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_room_check_serializer_invalid_date_end_before_start():

    invalid_start = date.today()
    invalid_end = invalid_start - timedelta(days=1)

    serializer = RoomBookingCheckSerializer(
        data={"start": invalid_start.isoformat(), "end": invalid_end.isoformat()}
    )

    with pytest.raises(serializers.ValidationError):
        serializer.is_valid(raise_exception=True)
