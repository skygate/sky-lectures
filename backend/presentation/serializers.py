from rest_framework import serializers

from presentation.models import Presentation, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class PresentationSerializer(serializers.ModelSerializer):
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = Presentation
        fields = ["title", "description", "scheduled_on", "user", "tags"]

    def create(self, validated_data):
        instance = Presentation.objects.create(
            title=validated_data.get("title"),
            description=validated_data.get("description", ""),
            scheduled_on=validated_data.get("scheduled_on"),
            user=validated_data.get("user", None),
        )
        if validated_data.get("tags", None):
            tags = validated_data.pop("tags")
            for tag in tags:
                tag = Tag.objects.get_or_create(name=tag["name"])[0]
                instance.tags.add(tag)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.scheduled_on = validated_data.get(
            "scheduled_on", instance.scheduled_on
        )
        instance.user = validated_data.get("user", instance.user)
        if validated_data.get("tags", None):
            tags = validated_data.pop("tags")
            if not self.partial:
                instance.tags.clear()
            for tag in tags:
                tag = Tag.objects.get_or_create(name=tag["name"])[0]
                instance.tags.add(tag)

        instance.save()
        return instance
