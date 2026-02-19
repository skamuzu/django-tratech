from django.db import models

class Enrollments(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="enrollments")
    student = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course", "student"],
                name="unique_enrollment",
            )
        ]
    