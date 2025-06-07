from rest_framework import serializers
from ..models import PopUp

class PopUpListSerializers(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = '__all__'

class PopUpRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = '__all__'

class PopUpWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = '__all__'