from rooms.serializers import RoomSerializer
from .models import Booking
from rest_framework import serializers
from datetime import date

class BookingReadSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Booking
        fields = ['id', 'room', 'first_name', 'last_name', 'start', 'end']


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['room', 'start', 'end']
    
    def validate(self, data):

        if data['start'] >= data['end']:
            raise serializers.ValidationError("Invalid date")
        
        if data['end'] < date.today():
            raise serializers.ValidationError("Invalid date")
        if data['start'] < date.today():
            raise serializers.ValidationError("Invalid date")

        overlapping_bookings = Booking.objects.filter(
            room=data['room'],
            start__lt=data['end'],
            end__gt=data['start']
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("Room is already booked")
        return data

