from rest_framework import generics, status, permissions
from rest_framework.response import Response
from apps.identity.serializers import UserSignupSerializer

class SignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        request.user.id = user.id

        return Response({'message': 'Account created successfully.'}, status=status.HTTP_201_CREATED)
