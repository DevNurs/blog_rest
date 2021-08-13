from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    profile = models.ImageField(upload_to='profiles', blank=True, null=True)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.username}"
