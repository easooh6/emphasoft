import pytest
from datetime import date, timedelta
from django.contrib.auth.models import User
from rooms.models import Room
from bookings.models import Booking
from bookings.serializers import BookingCreateSerializer


@pytest.fixture
def room(db):
    return Room.objects.create(name="Standard", price=3000, capacity=2)


@pytest.mark.django_db
def test_valid_data(room):
    data = {
        "room": room.id,
        "start": date.today() + timedelta(days=1),
        "end": date.today() + timedelta(days=3),
    }
    s = BookingCreateSerializer(data=data)
    assert s.is_valid(), s.errors


@pytest.mark.django_db
def test_start_after_end(room):
    data = {
        "room": room.id,
        "start": date.today() + timedelta(days=3),
        "end": date.today() + timedelta(days=1),
    }
    s = BookingCreateSerializer(data=data)
    assert not s.is_valid()


@pytest.mark.django_db
def test_dates_in_past(room):
    data = {
        "room": room.id,
        "start": date.today() - timedelta(days=3),
        "end": date.today() - timedelta(days=1),
    }
    s = BookingCreateSerializer(data=data)
    assert not s.is_valid()


@pytest.mark.django_db
def test_overlap(room):
    user = User.objects.create_user(username="u", password="p")
    Booking.objects.create(
        user=user,
        room=room,
        start=date.today() + timedelta(days=1),
        end=date.today() + timedelta(days=3),
    )
    data = {
        "room": room.id,
        "start": date.today() + timedelta(days=2),
        "end": date.today() + timedelta(days=4),
    }
    s = BookingCreateSerializer(data=data)
    assert not s.is_valid()
