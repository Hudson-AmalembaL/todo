from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User
from .forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["id", "email", "username", "last_name"]
    list_display_links = ["email", "username"]

    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                    "username",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )


admin.site.register(User, UserAdmin)
