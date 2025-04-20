from django.apps import AppConfig


class VerificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Helpers.verification'

    def ready(self):
        import Helpers.verification.signals
