from django.db import models
from django.contrib.auth.models import AbstractUser
from .manegers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True,error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)
    



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
