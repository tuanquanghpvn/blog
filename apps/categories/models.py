from django.db import models
from apps.core.models import (Describable, Timestampable)


# Create your models here.

class Category(Describable, Timestampable):

   class Meta:
       verbose_name = 'Category'
       verbose_name_plural = 'Categories'
       db_table = 'category'
