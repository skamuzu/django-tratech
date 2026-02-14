from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from .models import Course
from .serializers import CourseSerializer
import cloudinary.uploader

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_parsers(self):
        action = getattr(self, "action", None)

        if action in ["create", "update", "partial_update"]:
            return [MultiPartParser(), FormParser(), JSONParser()]


    def _handle_image_upload(self, request):
        file = request.FILES.get("image")
        if file:
            upload_data = cloudinary.uploader.upload(file)
            request.data["image"] = upload_data["secure_url"]

    def create(self, request, *args, **kwargs):
        self._handle_image_upload(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self._handle_image_upload(request)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self._handle_image_upload(request)
        return super().partial_update(request, *args, **kwargs)
