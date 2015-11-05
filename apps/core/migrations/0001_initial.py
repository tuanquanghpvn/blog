# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False, related_name='profile')),
                ('avatar', models.ImageField(upload_to='avatar', max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'UserProfile',
                'db_table': 'user_profile',
                'verbose_name_plural': 'UserProfiles',
            },
        ),
    ]
