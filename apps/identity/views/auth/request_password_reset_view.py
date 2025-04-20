from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from apps.identity.serializers import PasswordResetRequestSerializer
from apps.identity.signals.user_signals import password_reset_requested

User = get_user_model()

class PasswordResetRequestView(generics.CreateAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(email=serializer.validated_data.get('email'))
        except User.DoesNotExist:
            return Response({'error': 'No account found with this email.'}, status=status.HTTP_404_NOT_FOUND)

        # send the actual user object now
        password_reset_requested.send(sender=self.__class__, user=user)

        return Response({'message': 'Password reset email sent.'}, status=status.HTTP_200_OK)
