from .auth import ViewSignup
from .auth import ViewLogout
from .auth import ViewLogin
from .auth import ResetRequestPasswordView
from .auth import ResetConfirmPasswordView

from .profile_views import ProfileView,UpdateProfileView

__all__ = [
    'ViewSignup',
    'ViewLogin',
    'ViewLogout',
    'ResetRequestPasswordView',
    'ResetConfirmPasswordView',
    'ProfileView',
    'UpdateProfileView',
]
