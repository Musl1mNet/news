from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from news.validators import PhoneValidator
class UserManager(BaseUserManager):
    pass


class User(AbstractUser):
    objects = UserManager()
    phone = models.CharField(max_length=14, default=None, null=True, unique=True, validators=[PhoneValidator()])
