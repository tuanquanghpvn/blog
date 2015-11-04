from django.db import models

from apps.core.models import (Describable, Timestampable)

class Tag(Describable):

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'
