from rest_framework.viewsets import ModelViewSet
from .serializers import ModuleSerializer
from .models import Module

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer