from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
# Módelo de usuario a medida
# usamos email en lugar de username


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email), **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra)

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    username = None
    email = models.EmailField(unique=True)
    objects = UserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email