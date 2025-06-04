from rest_framework import serializers
from ..models import Service_management
from .other_serializers import OtherImageSerializer

class ServiceManagementListSerializer(serializers.ModelSerializer):
    Other_image = OtherImageSerializer(many=True, read_only=True)
    class Meta:
        model = Service_management
        fields = ['S.N.', 'Name', 'Category', 'Sub-Category', 'Price', 'Description', 'Feature_images', 'Other_image']

class ServiceManagementRetrieveSerializer(serializers.ModelSerializer):
    Other_image = OtherImageSerializer(many=True, read_only=True)
    class Meta:
        model = Service_management
        fields = '__all__'