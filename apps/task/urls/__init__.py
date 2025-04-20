from .tag_urls import urlpatterns as tag_urls
from .task_urls import urlpatterns as task_urls
from .sub_task_urls import urlpatterns as sub_task_urls


urlpatterns = task_urls + sub_task_urls + tag_urls


__all__ = ['urlpatterns']