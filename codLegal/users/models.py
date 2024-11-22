from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    dob = models.DateField(null=True, verbose_name='Date of birth')

    REQUIRED_FIELDS = ["email", "dob"]