from rest_framework import serializers
from rooms.models import Room
from datetime import date


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class RoomBookingCheckSerializer(serializers.Serializer):
    start = serializers.DateField()
    end = serializers.DateField()

    def validate(self, data):
        if data["start"] >= data["end"]:
            raise serializers.ValidationError("Invalid data")
        if data["start"] < date.today():
            raise serializers.ValidationError("Invalid data")
        return data
