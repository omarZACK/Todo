from rest_framework import serializers
from ..models import TagModel
from Helpers.structure.serializers import TrackingSerializerMixin


class TagSerializer(TrackingSerializerMixin,serializers.ModelSerializer):
    name = serializers.CharField(max_length=255,required=True)
    class Meta:
        model = TagModel
        fields= ['id','name',]

    def validate_name(self, value):
        value = value.lower().strip()
        if not value:
            raise serializers.ValidationError("Tag name cannot be empty")
        return value
