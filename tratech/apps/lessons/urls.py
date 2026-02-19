from rest_framework.routers import SimpleRouter
from .views import LessonViewSet

router = SimpleRouter()

router.register(r"lessons", LessonViewSet)

urlpatterns = router.urls