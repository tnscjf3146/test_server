from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=10, unique=True)
    profile_image = models.ImageField(upload_to='user/profiles/', blank=True, null=True)
    