__all__ = ['UserSignupSerializer','UserLoginSerializer',
           'PasswordResetConfirmSerializer',
           'PasswordResetRequestSerializer']

from prompt_toolkit.layout.processors import AppendAutoSuggestion
from rest_framework import serializers as ser
from django.contrib.auth import get_user_model as gum, authenticate as auth
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password as valid_password
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator as Uv
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as TokenSerializer

from apps.identity.models.enums import GenderChoices

User = gum()

# Signup Serializer
class UserSignupSerializer(ser.ModelSerializer):
    name = ser.CharField(required=True, max_length=100)
    email = ser.EmailField(required=True,validators=[
        Uv(queryset=User.objects.all())
    ])
    password = ser.CharField(write_only=True, min_length=8,validators=[valid_password])
    gender = ser.ChoiceField(
        choices=GenderChoices,
        required=False,
        allow_null=True,
        default=None
    )
    class Meta:
        model = User
        fields = ['email','name', 'password','gender']

    # def validate(self, attrs):
    #     if 'gender' in attrs:
    #         attrs['gender'] = attrs['gender'].lower()
    #         if attrs['gender'] not in GenderChoices.values():
    #             raise ValidationError(_('Invalid gender choice'))
    #     return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            gender=validated_data.get('gender')
        )
        return user

# Login Serializer
class UserLoginSerializer(TokenSerializer):
    username_field = 'email'  # important if your USERNAME_FIELD = 'email'

    def validate(self, attrs):
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        user = auth(
            request=self.context.get('request'),
            email=credentials['email'],
            password=credentials['password']
        )

        if not user:
            raise ser.ValidationError(
                {'detail': _("Invalid email or password.")},
                code='authorization'
            )

        if not user.is_active:
            raise ser.ValidationError(
                {'detail': _("User account is disabled.")},
                code='authorization'
            )
        refresh = self.get_token(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'Login successful.'
        }

        return data


# Password Reset Request Serializer
class PasswordResetRequestSerializer(ser.Serializer):
    email = ser.EmailField(required=True)



# Password Reset Confirm Serializer
class PasswordResetConfirmSerializer(ser.Serializer):
    email = ser.EmailField()
    code = ser.CharField()
    new_password = ser.CharField(write_only=True, min_length=8)