from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "room", "start", "end")

    list_filter = ("start", "user", "room")

    search_fields = ("user__username", "room__name")
