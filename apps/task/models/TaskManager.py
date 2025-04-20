__all__ = ['TaskManager']

from django.db import models, transaction
from django.utils import timezone as tz
from datetime import timedelta as td

class TaskQuerySet(models.QuerySet):
    def overdue(self):
        return self.filter(due_date__lte=tz.now()).exclude(status='done')

    def upcoming(self, days=7):
        return self.filter(
            due_date__gt=tz.now(),
            due_date__lte=tz.now() + td(days=days)
        )
    def by_status(self, status):
        return self.filter(status=status)
    def by_priority(self, priority):
        return self.filter(priority=priority)
    def recurring(self):
        return self.filter(is_recurring=True)
    def for_user(self, user):
        return self.filter(creator=user)

class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)

    def overdue(self):
        return self.get_queryset().overdue()

    def upcoming(self, days=7):
        return self.get_queryset().upcoming(days)

    def by_priority(self, priority):
        return self.get_queryset().by_priority(priority)

    def by_status(self, status):
        return self.get_queryset().by_status(status)

    def recurring(self):
        return self.get_queryset().recurring()

    def for_user(self, user):
        return self.get_queryset().for_user(user)

    def create_task(self, creator, title, description=None, due_date=None,
                                 priority="medium", status="todo", is_recurring=False,
                                 tags=None, subtasks=None):
        with transaction.atomic():
            """
            Create a task with optional subtasks and tags.
            - If a tag exists, it links it. If not, creates it and sets creator as created_by
            - Adds creator to the tag's users many-to-many relationship
            - Subtasks are created and linked to the task.
            """

            # Create task
            task = self.create(
                creator=creator,
                title=title,
                description=description,
                due_date=due_date or (tz.now() + td(days=10)),
                priority=priority,
                status=status,
                is_recurring=is_recurring
            )
            from ..models import TagModel, SubTaskModel

            # Handle tags
            if tags:
                for tag_name in tags:
                    # Get or create tag with creator set immediately
                    tag, created = TagModel.objects.get_or_create(
                        name=tag_name,
                        defaults={'created_by': creator}  # Set creator on creation
                    )

                    task.tags.add(tag)
                    tag.users.add(creator)  # Add creator to users M2M

                    # For existing tags, update created_by if null
                    if not created and not tag.created_by:
                        tag.created_by = creator
                        tag.save()

            # Handle subtasks
            if subtasks:
                for subtask_title in subtasks:
                    SubTaskModel.objects.create(task=task, title=subtask_title)

            return task
