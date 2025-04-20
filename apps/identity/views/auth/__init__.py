from .login_view import LoginView as ViewLogin
from .signup_view import SignupView as ViewSignup
from .logout_view import LogoutView as ViewLogout
from .request_password_reset_view import PasswordResetRequestView as ResetRequestPasswordView
from .request_password_confirm_view import ResetPasswordConfirmView as ResetConfirmPasswordView


__all__ = [
    'ViewLogin',
    'ViewSignup',
    'ViewLogout',
    'ResetRequestPasswordView',
    'ResetConfirmPasswordView',
]