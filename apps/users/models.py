import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    email = models.EmailField(verbose_name=_("Email address"), unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=30)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    objects = CustomUserManager()

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def __str__(self):
        return f"{self.username}"
