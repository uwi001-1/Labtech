from rest_framework import viewsets
from ..models import FAQ
from ..serializers.faq_serializers import FAQListSerializers, FAQRetrieveSerializers, FAQWriteSerializers

from booking.utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class bookingManagementViewsets(viewsets.ModelViewSet):
    serializer_class = FAQListSerializers
    queryset = FAQ.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return FAQWriteSerializers
        elif self.action == 'retrieve':
            return FAQRetrieveSerializers
        return super().get_serializer_class()
    