from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.request import Request
from bookings.models import Booking
from rest_framework.views import APIView, status
from bookings.serializers import BookingCreateSerializer, BookingReadSerializer


class BookingListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request) -> Response:
        bookings = Booking.objects.filter(user=request.user).select_related("room")

        serializer = BookingReadSerializer(bookings, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = BookingCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)

            read_serializer = BookingReadSerializer(serializer.instance)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)


class BookingDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request, id: int) -> Response:
        booking = get_object_or_404(Booking, id=id, user=request.user)

        serializer = BookingReadSerializer(booking)

        return Response(serializer.data)

    def delete(self, request: Request, id: int) -> Response:

        booking = get_object_or_404(Booking, id=id, user=request.user)

        booking.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
