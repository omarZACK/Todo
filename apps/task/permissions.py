from rest_framework import permissions
from .models import TaskModel


class IsTaskOwner(permissions.BasePermission):
    """
    Custom permission to only allow task owners to edit or delete their tasks and related subtasks.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS like GET, HEAD, OPTIONS are allowed for everyone authenticated
        if request.method in permissions.SAFE_METHODS:
            return True

        # If this is a Task object, check creator
        if hasattr(obj, 'creator'):
            return obj.creator == request.user

        # If this is a SubTask object, check its task's creator
        if hasattr(obj, 'task'):
            return obj.task.creator.id == request.user.id

        # If object is neither Task nor SubTask — deny by default
        return False

    def has_permission(self, request, view):
        # First check if user is authenticated
        if not bool(request.user and request.user.is_authenticated):
            return False

        # For creation, we need to check the task_id parameter
        if view.action == 'create':
            task_id = request.query_params.get('task_id')
            if not task_id:
                return False

            try:
                task = TaskModel.objects.get(id=task_id)
                return task.creator == request.user
            except TaskModel.DoesNotExist:
                return False

        return True


class IsTagOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(obj, 'task'):
            return obj.task.creator.id == request.user.id
        return False
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)