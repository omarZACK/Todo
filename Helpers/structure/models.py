from django.db import models as m


class TrackingModel(m.Model):
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']