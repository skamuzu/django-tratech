from django.db import models
from uuid import uuid4
from django.utils.text import slugify

class Lesson(models.Model):
   
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    content = models.JSONField(blank=True, null=True)
    lesson_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    module = models.ForeignKey("Module",  on_delete=models.CASCADE, related_name="lessons")
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
            
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["lesson_number", "module"],
                name="unique_lesson_per_module"
            )
        ]
            
    def __str__(self):
        return self.name