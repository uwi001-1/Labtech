from rest_framework import viewsets
from ..models import MeetTheTeam
from ..serializers.meet_serializers import MeetTheTeamListSerializers, MeetTheTeamRetrieveSerializers, MeetTheTeamWriteSerializers

from booking.utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class bookingManagementViewsets(viewsets.ModelViewSet):
    serializer_class = MeetTheTeamListSerializers
    queryset = MeetTheTeam.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MeetTheTeamWriteSerializers
        elif self.action == 'retrieve':
            return MeetTheTeamRetrieveSerializers
        return super().get_serializer_class()
    