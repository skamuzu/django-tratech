from django.db import models

from uuid import uuid4

class Lesson(models.Model):
   
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    content = models.JSONField(blank=True, null=True)
    lesson_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    module = models.ForeignKey("modules.Module",  on_delete=models.CASCADE, related_name="lessons")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["lesson_number", "module"],
                name="unique_lesson_per_module"
            )
        ]
            
    def __str__(self):
        return self.name
    
    
class Progress(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="lesson_progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="user_progress")
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "lesson"],
                name="unique_progress",
            )
        ]
    