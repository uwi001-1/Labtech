from rest_framework import viewsets
from ..models import BannerText
from ..serializers.banner_serializers import BannerTextListSerializers, BannerTextRetrieveSerializers, BannerTextWriteSerializers

from banner.utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class bannerViewsets(viewsets.ModelViewSet):
    serializer_class = BannerTextListSerializers
    queryset = BannerText.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BannerTextWriteSerializers
        elif self.action == 'retrieve':
            return BannerTextRetrieveSerializers
        return super().get_serializer_class()