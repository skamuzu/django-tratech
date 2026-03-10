from apps.coursework.models import Lesson
from django.utils.text import slugify

def run():
    lessons = Lesson.objects.all()
    
    for lesson in lessons:
        lesson.slug = slugify(lesson.name)
        lesson.save(update_fields=["slug"])