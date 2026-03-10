from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import CourseGeneralView, CourseSpecificView, CourseModuleView
from .views import LessonViewSet, ModuleViewSet

urlpatterns = [
    path("courses/", CourseGeneralView.as_view()),
    path("courses/<slug:slug>/", CourseSpecificView.as_view()),
    path("courses/<slug:slug>/modules/", CourseModuleView.as_view()),
]

router = SimpleRouter()
router.register(r"lessons", LessonViewSet)
router.register(r"modules",ModuleViewSet)

urlpatterns += router.urls