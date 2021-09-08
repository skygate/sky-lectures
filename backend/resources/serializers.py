from rest_framework import serializers

from resources.models import Resource, Presentation


class ResourceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = Resource.object.create(
            name=validated_data.get("name"),
            description=validated_data.get("description"),
            path=validated_data.get("path"),
            uploaded_on=validated_data.get("uploaded_on"),
        )
        if validated_data.get("resource", None):
            resources = validated_data.pop("resources")
            for res in resources:
                res = Resource.objects.get_or_create(name=res["name"])[0]
                instance.resources.add(res)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.uploaded_on = validated_data.get("uploaded_on", instance.uploaded_on)
        instance.user = validated_data.get("user", instance.user)
        if validated_data.get("resources", None):
            resources = validated_data.pop("resources")
            if not self.partial:
                instance.resources.clear()
            for res in resources:
                res = Resource.objects.get_or_create(name=res["name"])[0]
                instance.resources.add(res)
        instance.save()

        return instance


class PresentationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = Presentation.object.create(
            name=validated_data.get("name")
        )
        instance.save()

        return instance
