from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from news.validators import PhoneValidator
from django.core.validators import ValidationError
class UserManager(BaseUserManager):
    def __create_user(self, username, password, *args, **kwargs):
        username = PhoneValidator.clean(username)
        if PhoneValidator.validate(username):
            raise ValidationError("Phone number error!")
        user = User(username=username, **kwargs)
        user.set_password(password)
        user.save()

    def create_user(self, *args, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)

        if kwargs.get('is_staff') or kwargs.get('is_superuser'):
            raise ValidationError("ERROR")

        return self.__create_user(*args, **kwargs)
    def create_seperuser(self, *args, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if not kwargs.get('is_staff') or not kwargs.get('is_superuser'):
            raise ValidationError("ERROR")

        return self.__create_user(*args, **kwargs)
class User(AbstractUser):
    objects = UserManager()
    phone = models.CharField(max_length=14, default=None, null=True, unique=True, validators=[PhoneValidator()])
