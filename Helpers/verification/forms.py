from django import forms as form


class VerifyCodeForm(form.Form):
    email = form.EmailField(widget=form.HiddenInput())
    code = form.CharField(
        max_length=6,
        min_length=6,
        required=True,
        widget=form.TextInput(attrs={
            'placeholder': 'Enter the verification code',
            'id': 'code'
        })
    )

    def clean_code(self):
        code = self.cleaned_data['code']
        if not code.isalnum():
            raise form.ValidationError("Verification code must be alphanumeric.")
        return code