from rest_framework import generics, permissions
from apps.identity.permissions.custom_permissions import IsOwnerOrReadOnly
from apps.identity.serializers import ProfileSerializer
from django.contrib.auth import get_user_model as gum

User = gum()

# View Profile
class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user


# Update Profile
class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the current authenticated user
        return self.request.user
