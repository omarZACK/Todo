from django.urls import path
from Helpers.verification.views import *

urlpatterns = [
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),
    path('resend-verify-code/', ResendVerificationCodeAPIView.as_view(), name='resend-verification-code'),
]