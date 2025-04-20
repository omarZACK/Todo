from django.conf import settings
from django.db import models
from Helpers.structure.models import TrackingModel as Tracking
from .TaskManager import TaskManager
from .enums import Priority ,Status
from .tag_model import Tag
from django.utils import timezone
from datetime import timedelta

def default_due_date():
    return timezone.now() + timedelta(days=10)

# Create your models here.

class Task(Tracking):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(default=default_due_date)
    priority = models.CharField(
        choices=Priority.choices, default=Priority.MEDIUM,max_length=15,
        error_messages={"Invalid_choice":f"Priority must be one of: {Priority.values()}"}
    )
    status = models.CharField(
        choices=Status.choices, default=Status.TODO,max_length=15,
        error_messages = {"Invalid_choice": f"Status must be one of: {Status.values()}"}
    )
    is_recurring = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    objects = TaskManager()

    def __str__(self):
        return self.title
