from datetime import timedelta as td
from django.contrib.auth import get_user_model as gum
from django.db import models
from django.utils import timezone as tz
from django.utils.crypto import get_random_string as grt
from Helpers.structure.models import TrackingModel as Tkm

User = gum()

def generate_verification_code():
    return grt(6, '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

class VerificationCode(Tkm):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verification_code')
    code = models.CharField(max_length=6, default=generate_verification_code)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = tz.now() + td(minutes=10)
        super().save(*args, **kwargs)

    def is_expired(self):
        if self.expires_at < tz.now():
            return True
        return False

    def __str__(self):
        return f"Code for ({self.user.email}, {self.code})"