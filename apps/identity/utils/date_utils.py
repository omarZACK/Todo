from datetime import timedelta
from django.utils import timezone

def get_current_datetime():
    """Return the current timezone-aware datetime."""
    return timezone.now()

def get_future_datetime(minutes=10):
    """Return datetime N minutes in the future."""
    return timezone.now() + timedelta(minutes=minutes)

def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"):
    if dt is None:
        return None
    local_dt = timezone.localtime(dt)
    return local_dt.strftime(fmt)

def is_expired(expiry_time):
    """Check if a given datetime is in the past."""
    return timezone.now() > expiry_time
