# urls.py
from rest_framework.routers import DefaultRouter
from ..views import SubTaskViewSet

router = DefaultRouter()
router.register(r'subtasks', SubTaskViewSet, basename='subtask')

urlpatterns = router.urls