# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(to='core.UserProfile'),
            preserve_default=False,
        ),
    ]
