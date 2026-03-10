from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Course, Lesson, Module
from .serializers import CourseGeneralSerializer, CourseSpecificSerializer, CourseWithModulesSerializer, LessonGeneralSerializer, ModuleListSerializer, ModuleSerializer

class CourseGeneralView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseGeneralSerializer

   
class CourseSpecificView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSpecificSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    
class CourseModuleView(RetrieveAPIView):
    serializer_class = CourseWithModulesSerializer
    lookup_field = 'slug'
    queryset = Course.objects.all()
    


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonGeneralSerializer
    lookup_field = "slug"


class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer