from django.dispatch.dispatcher import receiver,Signal
from django.conf import settings
from urllib.parse import urlencode
from base64 import urlsafe_b64encode
from django.contrib.auth.tokens import default_token_generator
from Helpers.services.email_send_by_yagmail import send_custom_email

password_reset_requested = Signal()


@receiver(password_reset_requested)
def send_password_reset_email(sender, user, **kwargs):
    encoded_email = urlsafe_b64encode(user.email.encode()).decode()
    token = default_token_generator.make_token(user)
    subject = 'Reset your password'
    query_params = urlencode({'email': encoded_email, 'token': token})
    reset_link = f"{settings.FRONTEND_URL}/auth/reset-password-confirm/?{query_params}"
    template_name = 'identity/email/password_reset_email.html'

    send_custom_email(
        subject=subject,
        user=user,
        template_name=template_name,
        link=reset_link
    )
