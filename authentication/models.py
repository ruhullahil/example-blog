from django.db import models
from django.contrib.auth.models import AbstractUser
from .manegers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
