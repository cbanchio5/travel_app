from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # For example, add a profile picture
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username
