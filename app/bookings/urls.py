from django.urls import path
from .views import BookingDetailAPIView, BookingListCreateAPIView

urlpatterns = [
    path("", BookingListCreateAPIView.as_view(), name="booking list"),
    path("<int:id>/", BookingDetailAPIView.as_view(), name="booking detail"),
]
