from django.db import models

from apps.core.models import (Describable, Timestampable)

class Tag(Describable):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'
