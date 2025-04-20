from rest_framework_simplejwt.views import TokenObtainPairView as _TokenObtainPairView
from rest_framework import permissions
from apps.identity.serializers.auth_serializers import UserLoginSerializer

class LoginView(_TokenObtainPairView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Check if authentication succeeded (status 200)
        if response.status_code == 200:
            response.data['message'] = 'Login successful.'

        return response