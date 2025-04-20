from rest_framework.generics import GenericAPIView as GenericView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model as gum
from ..models import VerificationCode as VerificationCodeModel
from ..signals import send_verification_email_signal

# create your views here


User = gum()

class ResendVerificationCodeAPIView(GenericView):
    queryset = VerificationCodeModel.objects.all()

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'No user found with this email.'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_active:
            return Response({'message': 'This account is already verified.'}, status=status.HTTP_200_OK)

        code, created = self.get_queryset().get_or_create(user=user)
        code.save()
        send_verification_email_signal(user,True)

        return Response({
            'message': 'Verification code resent successfully.',
            'code': code.code
        }, status=status.HTTP_200_OK)