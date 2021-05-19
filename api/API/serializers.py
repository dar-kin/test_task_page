from rest_framework import serializers
from page import models


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ["text", "file"]


class PageSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    class Meta:
        model = models.Page
        fields = ["name", "label", "contents"]
