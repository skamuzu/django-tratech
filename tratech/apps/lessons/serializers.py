from rest_framework import serializers
from .models import Lesson

class LessonGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        
class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["name","slug"]
        