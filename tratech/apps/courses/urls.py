from django.urls import path
from .views import CourseGeneralView, CourseSpecificView

urlpatterns = [
    path("", CourseGeneralView.as_view()),
    path("<slug:slug>/", CourseSpecificView.as_view())
]