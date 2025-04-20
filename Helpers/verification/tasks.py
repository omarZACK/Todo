# Helpers/verification/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import VerificationCode

@shared_task
def delete_expired_verification_codes():
    expired_count, _ = VerificationCode.objects.filter(expires_at__lt=timezone.now()).delete()
    return f"{expired_count} expired verification codes deleted."
