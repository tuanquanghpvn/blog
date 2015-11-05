from django.db import models
from django.conf import settings

from apps.core.models import (Describable, Timestampable, UserProfile)
from apps.categories.models import Category

# Create your models here.

class Products(Describable, Timestampable):
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to=settings.PRODUCT_DIR, max_length=255,
                                                                blank=False)
    price = models.FloatField(blank=False, null=False, default=0.0)
    profile = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'

    

