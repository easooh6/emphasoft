from rooms.serializers import RoomSerializer,RoomBookingCheckSerializer
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rooms.models import Room
from bookings.models import Booking
from rest_framework.pagination import PageNumberPagination

class RoomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = RoomPagination

    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'capacity': ['exact'],
        'price': ['gte', 'lte', 'exact'],
    }
    ordering_fields = ['price', 'capacity']

    def get_queryset(self):
        queryset = super().get_queryset()

        start_date = self.request.query_params.get('start')
        end_date = self.request.query_params.get('end')
        if start_date and end_date:

            validation_serializer = RoomBookingCheckSerializer(data=self.request.query_params)
            validation_serializer.is_valid(raise_exception=True)

            data = validation_serializer.validated_data

            occupied_rooms_ids = Booking.objects.filter(
                start__lt=data["end"],
                end__gt=data["start"]
            ).values_list('room_id', flat=True)
            queryset = queryset.exclude(id__in=occupied_rooms_ids)

        return queryset
