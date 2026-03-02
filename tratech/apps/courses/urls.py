from django.urls import path
from .views import CourseGeneralView, CourseSpecificView, CourseModuleView

urlpatterns = [
    path("", CourseGeneralView.as_view()),
    path("<slug:slug>/", CourseSpecificView.as_view()),
    path("<slug:slug>/modules/", CourseModuleView.as_view()),
    
]