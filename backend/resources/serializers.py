from rest_framework import serializers

from resources.models import Resource
from presentation.models import Presentation


class UpdateResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = ['name', 'description', 'uploaded_on']


class CreateResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = ['name', 'description', 'path', 'uploaded_on', 'presentation']

    def create(self, validated_data):
        validated_data['presentation'] = Presentation.objects.get(validated_data['presentation'])
        return super().create(validated_data)
