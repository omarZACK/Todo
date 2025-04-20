from django.db import models
from Helpers.structure.models import TrackingModel as Tracking
from .task_model import Task

# Create your models here.

class SubTask(Tracking):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title