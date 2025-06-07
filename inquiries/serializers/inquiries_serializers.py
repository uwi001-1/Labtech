from rest_framework import serializers
from ..models import CustomerInquiries

class CustomerInquiriesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerInquiries
        fields = '__all__'

class CustomerInquiriesRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerInquiries
        fields = '__all__'

class CustomerInquiriesWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerInquiries
        fields = '__all__'