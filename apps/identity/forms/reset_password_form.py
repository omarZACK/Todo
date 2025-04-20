from django import forms as form
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class ResetPasswordForm(form.Form):
    password = form.CharField(
        widget=form.PasswordInput(attrs={'placeholder': 'New password', 'required': True}),
        min_length=8,
    )
    confirm_password = form.CharField(
        widget=form.PasswordInput(attrs={'placeholder': 'Confirm password', 'required': True}),
        min_length=8,
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
            password_validation.validate_password(password)

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')


        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
