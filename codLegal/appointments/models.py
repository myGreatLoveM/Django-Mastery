from django.db import models



class PracticeArea(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Name of Law",
    )
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(name="pa_name_unq", fields=("name", ))
        ]






