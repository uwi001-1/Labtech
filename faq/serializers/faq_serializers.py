from rest_framework import serializers
from ..models import FAQ

class FAQListSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'