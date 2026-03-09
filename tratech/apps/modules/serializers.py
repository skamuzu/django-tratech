from rest_framework import serializers
from apps.lessons.serializers import LessonListSerializer
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        
class ModuleListSerializer(serializers.ModelSerializer):
    lessons = LessonListSerializer(many=True)
    
    class Meta:
        model = Module
        fields = ['name', 'lessons', "total_lessons_in_module"]