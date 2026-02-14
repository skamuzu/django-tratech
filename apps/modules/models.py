from django.db import models
from uuid import uuid4

# Create your models here.
class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="modules"
    )