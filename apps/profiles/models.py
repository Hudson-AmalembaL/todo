from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampledUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "MALE", _("Male")
    FEMALE = "FEMALE", _("Female")
    OTHER = "OTHER", _("Other")


class Profile(TimeStampledUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(
        choices=Gender.choices, default=Gender.OTHER, max_length=20
    )
    phone_number = PhoneNumberField(default="+254746468686")

    def __str__(self):
        return f"{self.user.username}'s profile"
