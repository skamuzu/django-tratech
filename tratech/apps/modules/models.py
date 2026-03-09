from django.db import models
from apps.lessons.models import Lesson
from uuid import uuid4


# Create your models here.
class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    module_number = models.PositiveIntegerField(unique=True, default=1)
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="modules"
    )
    
    @property
    def total_lessons_in_module(self):
        return Lesson.objects.filter(module=self).count()
   

    def __str__(self):
        return self.name
