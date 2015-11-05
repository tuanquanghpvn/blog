# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
