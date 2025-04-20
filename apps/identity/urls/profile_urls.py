from django.urls import path
from apps.identity.views import ProfileView ,UpdateProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile_view'),  # View Profile
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update'),  # Update Profile
]
