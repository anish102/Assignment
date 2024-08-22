from rest_framework import serializers

from .models import FaceEmbed


# Serializer for the FaceEmbed model, including all fields in the serialization
class FaceEmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceEmbed
        fields = '__all__'
