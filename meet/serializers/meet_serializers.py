from rest_framework import serializers
from ..models import MeetTheTeam

class MeetTheTeamListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetTheTeam
        fields = '__all__'

class MeetTheTeamRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetTheTeam
        fields = '__all__'

class MeetTheTeamWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetTheTeam
        fields = '__all__'