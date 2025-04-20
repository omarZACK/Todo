from django.contrib.auth.tokens import default_token_generator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from urllib.parse import urlencode
from base64 import urlsafe_b64encode
from django.contrib.auth import get_user_model as gum
from .models import VerificationCode as Code
from Helpers.services.email_send_by_yagmail import send_custom_email

User = gum()

@receiver(post_save, sender=User)
def send_verification_email_signal(instance, created, **kwargs):
    if created and not instance.is_active:
        encoded_email = urlsafe_b64encode(instance.email.encode()).decode()
        token = default_token_generator.make_token(instance)
        base_url = f"{settings.FRONTEND_URL}/verification/verify-code/"
        query = urlencode({
            'email': encoded_email,
            'token': token
        })
        verification_link = f"{base_url}?{query}"
        subject = "Activate your account"
        send_custom_email(
            subject=subject,
            user=instance,
            template_name='verification/email/verification_email.html',
            link=verification_link
        )



@receiver(post_save, sender=User)
def create_verification_code(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'verification_code'):
        Code.objects.create(user=instance)