from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView as Trv
from apps.identity.views import (
    ViewLogout,
    ViewLogin,
    ViewSignup,
    ResetRequestPasswordView,
    ResetConfirmPasswordView
)

urlpatterns = [
    # Signup (POST request)
    path('signup/', ViewSignup.as_view(), name='signup'),

    # Login (POST request) - with JWT token generation
    path('login/', ViewLogin.as_view(), name='login'),

    # Logout (POST request) - with JWT token blacklist
    path('logout/', ViewLogout.as_view(), name='logout'),

    # Token Refresh (POST request) - for refreshing JWT token
    path('refresh/', Trv.as_view(), name='refresh_token'),

    # Request Password Reset (POST request)
    path('password-reset/', ResetRequestPasswordView.as_view(), name='password_reset_request'),

    # Reset Password Confirmation (GET and POST requests) - for resetting password
    path('reset-password-confirm/', ResetConfirmPasswordView.as_view(), name='reset-password-confirm'),
]
