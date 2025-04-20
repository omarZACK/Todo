from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..serializers import TaskSerializer
from ..models import TaskModel
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tags__name']

    def get_queryset(self):
        queryset = super().get_queryset().for_user(self.request.user)

        # Handle multiple tag filtering (AND condition)
        tag_names = self.request.query_params.get('tags')
        if tag_names:
            tags = [name.strip() for name in tag_names.split(',')]
            for tag in tags:
                queryset = queryset.filter(tags__name=tag)

        # Status filtering
        if 'status' in self.request.query_params:
            queryset = queryset.by_status(self.request.query_params['status'])
        # Priority filtering
        if 'priority' in self.request.query_params:
            queryset = queryset.by_priority(priority=self.request.query_params['priority'])

        return queryset

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        """Get all overdue tasks for the current user"""
        overdue_tasks = self.get_queryset().overdue()
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def recurring(self, request):
        """Get all overdue tasks for the current user"""
        overdue_tasks = self.get_queryset().recurring()
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)