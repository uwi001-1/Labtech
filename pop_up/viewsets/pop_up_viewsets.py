from rest_framework import viewsets
from ..models import PopUp
from ..serializers.pop_up_serializers import PopUpListSerializers, PopUpRetrieveSerializers, PopUpWriteSerializers

from booking.utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class popUpViewsets(viewsets.ModelViewSet):
    serializer_class = PopUpListSerializers()
    queryset = PopUp.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PopUpWriteSerializers
        elif self.action == 'retrieve':
            return PopUpRetrieveSerializers
        return super().get_serializer_class()
    