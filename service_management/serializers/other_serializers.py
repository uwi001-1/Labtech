from rest_framework import serializers
from ..models import OtherImage

class OtherImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherImage
        fields = ['id', 'image']