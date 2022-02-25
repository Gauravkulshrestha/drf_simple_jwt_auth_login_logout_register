from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=120, null=True)
    email = models.EmailField(max_length=120, unique=True)
    bio = models.TextField(max_length=255, null=True)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']