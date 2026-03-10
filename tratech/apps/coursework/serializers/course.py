from rest_framework import serializers
from apps.coursework.models import Course
from .module import ModuleListSerializer

class CourseGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ("course_info",)
        
class CourseSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseWithModulesSerializer(serializers.ModelSerializer):
    modules = ModuleListSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ("id", "name", "slug", "modules",'total_lessons_in_course')