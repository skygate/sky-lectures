from rest_framework import serializers

from presentation.models import Presentation, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class InputPresentationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True)
    scheduled_on = serializers.DateTimeField()
    tags = TagSerializer(required=False, many=True)

    class Meta:
        fields = ["title", "description", "scheduled_on", "tags"]


class OutputPresentationSerializer(serializers.ModelSerializer):
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = Presentation
        fields = ["title", "description", "scheduled_on", "user", "tags"]
        read_only_fields = fields
