from rest_framework import serializers
from apps.coursework.models import Module
from .lesson import LessonListSerializer

class ModuleListSerializer(serializers.ModelSerializer):
    lessons = LessonListSerializer(many=True)
    
    class Meta:
        model = Module
        fields = ['name', 'lessons', "total_lessons_in_module"]
    
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'