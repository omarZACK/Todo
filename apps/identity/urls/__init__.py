from .auth_urls import urlpatterns as auth_urls
from .profile_urls import urlpatterns as profile_urls


urlpatterns = auth_urls + profile_urls

__all__ = ['urlpatterns']