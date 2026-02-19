from django.db import models
from uuid import uuid4
from django_validated_jsonfield import ValidatedJSONField
from django.utils.text import slugify


class Course(models.Model):
    _course_info_schema_ = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": {"type": "string"},
            "answer": {"type": "string"},
            "answer_bullet_points": {
                "type": "array",
                "items": {"type": "string"}
            },
        },
        "required": ["question", "answer"],
        "additionalProperties": False,
    }
}


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    course_info = ValidatedJSONField(schema=_course_info_schema_)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField()
    published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
            

    def __str__(self):
        return self.name
