from rest_framework import serializers
from ..models import Service_management

class ServiceManagementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_management
        fields = ['S.N.', 'Name', 'Category', 'Sub-Category', 'Price', 'Description', 'Feature_images', 'Other_image']

class ServiceManagementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_management
        fields = '__all__'