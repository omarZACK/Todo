__all__ = ["VerifyCodeView"]

# Hidden (private) imports with aliases
from base64 import urlsafe_b64decode as b64decode
from django.contrib.auth import get_user_model as gum
from django.shortcuts import render as _render
from django.views import View as _View
from binascii import Error as BinasciiError
from Helpers.verification.models import VerificationCode
from Helpers.verification.forms import VerifyCodeForm

# Create your views here.

class VerifyCodeView(_View):
    template_name = "verification/verify_code.html"
    user_model = gum()

    def get(self, request):
        context = {}
        encoded_email = request.GET.get('email')
        if not encoded_email:
            context['error'] = "Invalid link."
            return _render(request, self.template_name, context)

        try:
            email = b64decode(encoded_email.encode()).decode()
            user = self.user_model.objects.get(email=email)
            context['form'] = VerifyCodeForm(initial={'email': email})
            if user.is_active:
                context['success'] = "Your account is already verified. You can log in."
            else:
                context['email'] = email
        except (BinasciiError, ValueError, self.user_model.DoesNotExist):
            context['error'] = "Invalid link format."

        return _render(request, self.template_name, context)

    def post(self, request):
        form = VerifyCodeForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            email = form.cleaned_data['email']
            code = form.cleaned_data['code']

            try:
                user = self.user_model.objects.get(email=email)
                verification = user.verification_code
            except self.user_model.DoesNotExist:
                context['error'] = "Verification failed. User not found."
                return _render(request, self.template_name, context)
            except VerificationCode.DoesNotExist:
                context['error'] = "No verification code associated with this account."
                return _render(request, self.template_name, context)

            if verification.code == code:
                user.is_active = True
                user.save()
                verification.delete()
                context['success'] = "Your account has been verified successfully!"
            else:
                context['error'] = "Invalid code."

            context['email'] = email
        else:
            context['error'] = "Please correct the errors below."

        return _render(request, self.template_name, context)

