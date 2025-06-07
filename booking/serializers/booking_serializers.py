from rest_framework import serializers
from ..models import BookingManagement

class BookingManagementListSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookingManagement
        fields = '__all__'

class BookingManagementRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookingManagement
        fields = '__all__'

class BookingManagementWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookingManagement
        fields = '__all__'