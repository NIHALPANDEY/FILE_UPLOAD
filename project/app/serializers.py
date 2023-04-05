from rest_framework import serializers
from .models import Attachment

class UploadAttachment(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"
    
    def create(self, validated_data):
        post = Attachment.objects.create(**validated_data)
        return post
