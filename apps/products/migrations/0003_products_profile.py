# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('products', '0002_auto_20151104_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='profile',
            field=models.ForeignKey(to='core.UserProfile'),
            preserve_default=False,
        ),
    ]
