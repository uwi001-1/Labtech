from rest_framework import serializers
from ..models import BannerText

class BannerTextSerializers(serializers.ModelSerializer):
    class Meta:
        model = BannerText
        fields = ['id', 'image_file', 'image_url', 'video_file', 'video_url', 'description']

    def validate(self, data):
        file = data.get('image_file')
        url = data.get('image_url')

        if file and url:
            raise serializers.ValidationError("Provide either an image file or an image URL, not both.")
        if not file and not url:
            raise serializers.ValidationError("You must provide either an image file or an image URL.")
        
        v_file = data.get('video_file')
        v_url = data.get('video_url')

        if v_file and v_url:
            raise serializers.ValidationError("Provide either an video file or an video URL, not both.")
        if not v_file and not v_url:
            raise serializers.ValidationError("You must provide either an video file or an video URL.")
        
        return data