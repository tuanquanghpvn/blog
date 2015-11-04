# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
                ('description', models.TextField(default='', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'db_table': 'tag',
                'verbose_name': 'Tag',
            },
        ),
    ]
