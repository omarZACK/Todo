__all__=['LogoutView']

from rest_framework_simplejwt.views import TokenBlacklistView as _TokenBlacklistView


class LogoutView(_TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data = {'message': 'Logged out successfully.'}
        return response