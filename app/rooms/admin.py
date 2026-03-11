from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "capacity")

    search_fields = ("name",)

    list_filter = ("capacity", "price")
