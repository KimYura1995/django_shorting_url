from rest_framework import serializers

from app_shortener_url.models import URLModel


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLModel
        fields = ['original_url']
