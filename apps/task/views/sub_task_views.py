from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import SubTaskModel, TaskModel
from ..permissions import IsTaskOwner
from ..serializers import SubTaskSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTaskModel.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsTaskOwner]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        task_id = self.request.query_params.get('task_id')
        if task_id:
            queryset = queryset.filter(task_id=task_id,task__creator_id=self.request.user.id)
        return queryset
    # POST /subtasks/?task_id=1 → Create subtask for task_id=1
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task_id = request.query_params.get('task_id')
        if not task_id:
            return Response(
                {"error": "task_id query parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        task = TaskModel.objects.get(id=task_id)
        self.perform_create(serializer, task=task)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, **kwargs):
        serializer.save(**kwargs)  # Saves with task=task

    # PATCH /subtasks/1/toggle/ → Toggle completion
    @action(detail=True, methods=['patch'])
    def toggle(self, request, pk=None):
        subtask = self.get_object()
        subtask.is_complete = not subtask.is_complete
        subtask.save()
        return Response(self.get_serializer(subtask).data)

