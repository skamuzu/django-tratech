from rest_framework import serializers
from apps.coursework.models import Lesson

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["name","slug","content"]

class LessonGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        