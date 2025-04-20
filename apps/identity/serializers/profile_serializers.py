__all__ = ['ProfileSerializer']

from rest_framework import serializers as ser
from django.contrib.auth import get_user_model as gum

User = gum()

class ProfileSerializer(ser.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'gender', 'created_at', 'updated_at']
        read_only_fields = ['id', 'email', 'created_at']

    def update(self, instance, validated_data):
        # You can add custom logic here for updating certain fields if needed
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        # Handling avatar or any other fields
        avatar = validated_data.get('avatar')
        if avatar:
            instance.avatar = avatar
        instance.save()
        return instance
