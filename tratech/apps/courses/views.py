from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from .models import Course
from .serializers import CourseGeneralSerializer, CourseSpecificSerializer
import cloudinary.uploader

class CourseGeneralView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseGeneralSerializer

   
class CourseSpecificView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSpecificSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"