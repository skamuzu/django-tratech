from rest_framework.viewsets import ModelViewSet
from .models import Lesson
from .serializers import LessonSerializer

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer