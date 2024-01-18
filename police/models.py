from django.contrib.auth.models import AbstractUser
from django.db import models

class myuser(AbstractUser):
    city = models.CharField(max_length=100)
    is_police = models.BooleanField(default=False)
    # Add any additional fields specific to your user profile model