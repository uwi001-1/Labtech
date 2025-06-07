from rest_framework import viewsets
from ..models import BookingManagement
from ..serializers.booking_serializers import BookingManagementListSerializers, BookingManagementRetrieveSerializers, BookingManagementWriteSerializers

from booking.utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class bookingManagementViewsets(viewsets.ModelViewSet):
    serializer_class = BookingManagementListSerializers
    queryset = BookingManagement.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]

    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookingManagementWriteSerializers
        elif self.action == 'retrieve':
            return BookingManagementRetrieveSerializers
        return super().get_serializer_class()
    