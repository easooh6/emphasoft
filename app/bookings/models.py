from django.db import models
from rooms.models import Room
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        unique=False,
    )
    start = models.DateField()
    end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["start", "end"]),
            models.Index(fields=["room", "start", "end"]),
        ]
