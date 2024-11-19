from django.db import models



class PracticeArea(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Name of Law",
    )
    description = models.TextField()


    class Meta:
        verbose_name = "Practice Area"
        verbose_name_plural = "Practice Areas"
        db_table = "appointments__practice_areas"
        constraints = [
            models.UniqueConstraint(name="pa_name_unq", fields=("name", ))
        ]

    def __str__(self):
        return f"{self.name}"





