from rest_framework import serializers as ser
from ..models import SubTaskModel
from Helpers.structure.serializers import TrackingSerializerMixin

class SubTaskSerializer(ser.ModelSerializer,TrackingSerializerMixin):
    title = ser.CharField(max_length=150)
    is_complete = ser.BooleanField(default=False)
    class Meta:
        model = SubTaskModel
        fields = ['id','title','is_complete']