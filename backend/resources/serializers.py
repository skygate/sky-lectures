from rest_framework import serializers

from resources.models import Resource
from presentation.models import Presentation


class UpdateResourceSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=100)
    uploaded_on = serializers.DateTimeField()

    class Meta:
        model = Resource
        fields = ['name', 'description', 'uploaded_on']


class CreateResourceSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=100)
    path = serializers.ImageField()
    uploaded_on = serializers.DateTimeField()
    fk_pres_id = serializers.UUIDField()

    class Meta:
        model = Resource
        fields = ['name', 'description', 'path', 'uploaded_on', 'fk_pres_id']

    def create(self, validated_data):
        validated_data['fk_pres_id'] = Presentation.objects.get(validated_data['fk_pres_id'])
        return super().create(validated_data)
