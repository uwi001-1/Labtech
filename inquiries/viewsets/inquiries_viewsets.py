from rest_framework import viewsets
from ..models import CustomerInquiries
from ..serializers.inquiries_serializers import CustomerInquiriesListSerializers, CustomerInquiriesRetrieveSerializers, CustomerInquiriesWriteSerializers

from booking.utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class customerInquiriesViewsets(viewsets.ModelViewSet):
    serializer_class = CustomerInquiriesListSerializers
    queryset = CustomerInquiries.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CustomerInquiriesWriteSerializers
        elif self.action == 'retrieve':
            return CustomerInquiriesRetrieveSerializers
        return super().get_serializer_class()
    