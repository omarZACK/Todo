from django.views import View as _View
from django.shortcuts import render as _render
from django.utils.http import urlsafe_base64_decode as b64decode
from django.utils.encoding import force_str as fs
from django.contrib.auth.tokens import default_token_generator as dtg
from django.contrib.auth import get_user_model as gum
from binascii import Error as BinasciiError
from apps.identity.forms.reset_password_form import ResetPasswordForm as Rpf

class ResetPasswordConfirmView(_View):
    template_name = 'identity/reset_password_confirm.html'
    user_model = gum()

    def get(self, request):
        encoded_email = request.GET.get('email')
        token = request.GET.get('token')
        context = {}

        if not encoded_email or not token:
            context['error'] = "Invalid or missing parameters."
            return _render(request, self.template_name, context)

        try:
            email = fs(b64decode(encoded_email))
            user = self.user_model.objects.get(email=email)
        except (BinasciiError, ValueError, self.user_model.DoesNotExist):
            context['error'] = "Invalid reset link."
            return _render(request, self.template_name, context)

        if not dtg.check_token(user, token):
            context['error'] = "Invalid or expired token."
            return _render(request, self.template_name, context)

        context.update({
            'form': Rpf(),
            'email': encoded_email,
            'token': token
        })
        return _render(request, self.template_name, context)

    def post(self, request):
        encoded_email = request.POST.get('email')
        token = request.POST.get('token')
        form = Rpf(request.POST)
        context = {}

        if not encoded_email or not token:
            context['error'] = "Invalid or missing parameters."
            return _render(request, self.template_name, context)

        if form.is_valid():
            try:
                email = fs(b64decode(encoded_email))
                user = self.user_model.objects.get(email=email)
            except (BinasciiError, ValueError, self.user_model.DoesNotExist):
                context['error'] = "Invalid reset link."
                return _render(request, self.template_name, context)

            if not dtg.check_token(user, token):
                context['error'] = "Invalid or expired token."
                return _render(request, self.template_name, context)

            user.set_password(form.cleaned_data['password'])
            user.save()

            context['success'] = "Password reset successful. You can now log in."
            return _render(request, self.template_name, context)

        # If form not valid, redisplay with errors
        context.update({
            'form': form,
            'email': encoded_email,
            'token': token
        })
        return _render(request, self.template_name, context)
