from rest_framework import viewsets
from ..models import Service_management
from ..serializers.service_serializers import ServiceManagementListSerializer, ServiceManagementRetrieveSerializer

class serviceViewsets(viewsets.ModelViewSet):
    serializer_class = ServiceManagementListSerializer
    queryset = Service_management.objects.all().order_by('-id')

    def get_queryset(self):
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ServiceManagementRetrieveSerializer
        return super().get_serializer_class()
