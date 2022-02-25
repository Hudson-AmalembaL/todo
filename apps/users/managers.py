from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(
        self, username, email, first_name, last_name, password, **extra_fields
    ):
        """
        Creates and saves a User with the given email, date of birth and password.
        """
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        if not username:
            raise ValueError(_("Users must submit a username"))

        if not first_name:
            raise ValueError(_("Users must have a first_name"))

        if not last_name:
            raise ValueError(_("Users must have a last name"))

        # Save the user to a model
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, email, first_name, last_name, password, **extra_fields
    ):
        """
        Creates and saves a superuser with the given email, date of birth and password
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address must be provided"))

        user = self.create_user(
            username, email, first_name, last_name, password, **extra_fields
        )
        user.save(using=self._db)
        return user
