from django.db import models
from Helpers.structure.models import TrackingModel as Tracking
from django.contrib.auth import get_user_model as gum
from django.db.models.functions import Lower

user = gum()

# Create your models here.

class Tag(Tracking):
    name = models.CharField(max_length=255, unique=True)
    created_by = models.OneToOneField(user,on_delete=models.CASCADE)
    users = models.ManyToManyField(user, related_name='tags')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='unique_lower_name',
            ),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)