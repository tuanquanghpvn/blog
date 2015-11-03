from django.db import models
from django.conf import settings

from apps.core.models import (Describable, Timestampable)
from apps.categories.models import Category

# Create your models here.
class Post(Describable, Timestampable):
    content = models.TextField
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to=settings.POST_DIR, blank=False, max_length=255)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'

