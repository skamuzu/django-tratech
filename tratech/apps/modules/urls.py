from django.urls import path
from .views import ModuleViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r"modules",ModuleViewSet)

urlpatterns = router.urls