from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_module_perms(self, users):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser
