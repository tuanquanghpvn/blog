from django.db import models
from django.conf import settings

# Create your models here.

class Timestampable(models.Model):
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Describable(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    description = models.TextField(blank=True, default='')

    class Meta:
        abstract = True

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True, related_name='profile')
    avatar = models.ImageField(upload_to=settings.AVATAR_DIR,
                                max_length=255, blank=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
        db_table = 'user_profile'
