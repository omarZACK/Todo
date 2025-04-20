from django.db import models
from apps.task.models import TaskModel
from Helpers.structure.models import TrackingModel as Tracking
from .enums import NotificationMethod

# Create your models here.

class Reminder(Tracking):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    remind_at = models.DateTimeField(null=False, blank=False)
    method = models.CharField(max_length=10, choices=NotificationMethod.choices, default=NotificationMethod.EMAIL)