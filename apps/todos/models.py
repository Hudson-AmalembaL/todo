from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampledUUIDModel


class Todo(TimeStampledUUIDModel):
    title = models.CharField(
        verbose_name=_("Todo Title"), max_length=50, blank=True, null=True
    )
    content = models.TextField(verbose_name=_("Todo Contents"), blank=False, null=False)

    def __str__(self):
        return self.title
