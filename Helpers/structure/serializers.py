from rest_framework import serializers


class TrackingSerializerMixin:
    def get_fields(self):
        # Get the base fields
        fields = super().get_fields()
        # Add the tracking fields dynamically
        fields['created_at'] = serializers.DateTimeField(read_only=True,required=False)
        fields['updated_at'] = serializers.DateTimeField(read_only=True,required=False)
        return fields
