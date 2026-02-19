from django.db import models

from uuid import uuid4

class Lesson(models.Model):
   
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    content = models.JSONField()
    lesson_number = models.PositiveIntegerField(unique=True,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    module = models.ForeignKey("modules.Module",  on_delete=models.CASCADE, related_name="lessons")
    
    def __str__(self):
        return self.name