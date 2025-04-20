from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from Helpers.structure.serializers import TrackingSerializerMixin
from .tag_serializer import TagSerializer
from .sub_task_serializer import SubTaskSerializer
from ..models import TaskModel
from ..models.enums import Priority,Status


class TaskSerializer(serializers.ModelSerializer,TrackingSerializerMixin):
    priority = serializers.CharField(required=False,allow_blank=True,max_length=15,default=Priority.MEDIUM)
    status = serializers.CharField(required=False,allow_blank=True,max_length=15,default=Status.TODO)
    is_recurring = serializers.BooleanField(default=False,required=False)
    tags = TagSerializer(many=True, required=False)
    subtasks = SubTaskSerializer(many=True, required=False)
    class Meta:
        model = TaskModel
        fields = ['id','title','description','due_date',
                  'priority','status','is_recurring','tags','subtasks']

    def validate(self, data):
        due_date = data.get('due_date')
        if 'priority' in data and data['priority'] == '':
            data['priority'] = 'low'
        if 'status' in data and data['status'] == '':
            data['status'] = 'todo'
        if due_date and due_date < timezone.now():
            raise ValidationError('Due date cannot be in the past.')
        if data.get('priority') and data['priority'] not in Priority.values():
            raise ValidationError(f'Priority must be one of the {Priority.values()}.')
        if data.get('status') and data['status'] not in Status.values():
            raise ValidationError(f'Status must be one of the {Status.values()}.')
        return data

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        subtasks_data = validated_data.pop('subtasks', [])

        tag_names = [tag['name'] for tag in tags_data]
        subtask_titles = [subtask['title'] for subtask in subtasks_data]

        task = TaskModel.objects.create_task(
            creator=self.context['request'].user,
            tags=tag_names,
            subtasks=subtask_titles,
            **validated_data
        )
        return task