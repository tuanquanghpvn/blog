from django.db import models
from apps.core.models import (Describable, Timestampable)


# Create your models here.

class Category(Describable, Timestampable):
   Choices = (
                (1, 'Post'),
                (2, 'Product')
           )
   type = models.IntegerField(choices=Choices, default=1)

   class Meta:
       verbose_name = 'Category'
       verbose_name_plural = 'Categories'
       db_table = 'category'
